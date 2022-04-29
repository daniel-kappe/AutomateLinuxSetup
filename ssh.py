#!/bin/env python3
from subprocess import run
from os.path import isfile, expandvars


def configure():
  ssh_key_path = expandvars('$HOME/.ssh/id_ed25519')
  if not isfile(ssh_key_path):
    run('ssh-keygen -t ed25519 -C "danielkappe@posteo.de"', shell=True, check=True)
    run('ssh-add ~/.ssh/id_ed25519', shell=True, check=True)


if __name__ == '__main__':
  configure()
