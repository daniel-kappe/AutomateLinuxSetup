#!/bin/env python3
from subprocess import run
from os.path import isfile, expandvars

def install():
  sauce_code_pro_path = expandvars('$HOME/.local/share/fonts/Sauce Code Pro Semibold Nerd Font Complete Mono.ttf')
  font_root_dir = expandvars('$HOME/.local/share/fonts')
  if not isfile(sauce_code_pro_path):
      run(f'wget https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/SourceCodePro/Semibold/complete/Sauce%20Code%20Pro%20Semibold%20Nerd%20Font%20Complete%20Mono.ttf --directory-prefix={font_root_dir}', shell=True, check=True)
      run('fc-cache -v', shell=True, check=True)

if __name__ == '__main__':
  install()
