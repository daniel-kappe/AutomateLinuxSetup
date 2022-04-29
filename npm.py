#!/bin/env python3
from subprocess import run

def configure():
  run("npm config set prefix='~/.npm-global'", shell=True, check=True)


if __name__ == '__main__':
  configure()

