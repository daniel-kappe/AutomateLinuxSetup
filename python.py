#!/bin/env python3
from subprocess import run


def install():
  run('pip install --user -U pip', shell=True, check=True)


if __name__ == '__main__':
  install()

