#!/bin/env python3
from subprocess import run
from os.path import isfile, expandvars


def install():
  run('pip install --user yubikey-manager', shell=True, check=True)
  yubikey_manager_path = expandvars('$HOME/.local/bin/yubikey-manager')
  yubikey_auth_path = expandvars('$HOME/.local/bin/yubikey-authenticator')
  if not isfile(yubikey_manager_path):
    run(f'wget -O {yubikey_manager_path} https://developers.yubico.com/yubikey-manager-qt/Releases/yubikey-manager-qt-latest-linux.AppImage', shell=True, check=True)
    run(f'chmod +x {yubikey_manager_path}', shell=True, check=True)
  if not isfile(yubikey_auth_path):
    run(f'wget -O {yubikey_auth_path} https://developers.yubico.com/yubioath-desktop/Releases/yubioath-desktop-latest-linux.AppImage', shell=True, check=True)
    run(f'chmod +x {yubikey_auth_path}', shell=True, check=True)


if __name__ == '__main__':
  install()
