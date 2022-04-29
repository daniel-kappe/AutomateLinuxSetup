#!/bin/env python3
from subprocess import run
from os.path import isdir, isfile, expandvars
from json import load


def install_docker():
  run('sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo', shell=True, check=True)
  run('sudo dnf install --assumeyes docker-ce docker-ce-cli containerd.io docker-compose-plugin', shell=True, check=True)
  if not isdir('/etc/docker'):
    run('sudo mkdir /etc/docker', shell=True, check=True)
  if not isfile('/etc/docker/daemon.json'):
      run("""echo '{
  "icc": false,
  "log-driver": "journald",
  "log-level": "info",
  "log-opts": {
    "tag": "{{.ImageName}}/{{.Name}}/{{.ID}}"
  },
  "live-restore": true,
  "data-root": "/var/lib/docker",
  "storage-driver": "overlay2",
  "userland-proxy": false,
  "no-new-privileges": true,
  "userns-remap": "default"
}' | sudo tee /etc/docker/daemon.json""", shell=True, check=True)
  run('sudo systemctl start docker', shell=True, check=True)
  run('sudo systemctl enable docker.service', shell=True, check=True)
  run('sudo systemctl enable containerd.service', shell=True, check=True)
  run('sudo usermod -aG docker $USER', shell=True, check=True)

def install():
  with open('./fedora_packages.json', 'r') as packages:
    package_list = load(packages)
  with open('/etc/dnf/dnf.conf', 'r') as dnf_conf:
    is_configured = 'fastestmirror=true' in dnf_conf.read()
  if not is_configured:
    with open('/etc/dnf/dnf.conf', 'a') as dnf_conf:
      dnf_conf.write('\n'.join(['fastestmirror=true', 'deltarpm=true', 'max_parallel_downloads=10']))
  run(['sudo dnf update', '--assumeyes'], shell=True, check=True)
  run('sudo dnf install --assumeyes https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm', shell=True, check=True)
  run('sudo dnf install --assumeyes https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm', shell=True, check=True)
  run(f'sudo dnf install --assumeyes {" ".join(package_list["dnf"])}', shell=True, check=True)
  run('flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo', shell=True, check=True)
  run(f'flatpak install --assumeyes flathub {" ".join(package_list["flatpak"]["flathub"])}', shell=True, check=True)
  install_docker()


if __name__ == '__main__':
  install()
