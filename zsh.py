#!/bin/env python3
from subprocess import run
from os.path import isdir, isfile, expandvars
from json import load


def install():
  if not isdir(expandvars('$HOME/.oh-my-zsh')):
    if not isfile('install.sh'):
      run('wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh', shell=True, check=True)
      run('chmod +x install.sh', shell=True, check=True)
    run('./install.sh --unattended', shell=True, check=True)
    run('sudo chsh -s /usr/bin/zsh $USER', shell=True, check=True)
  setup_autosuggestions()
  setup_zsh_theme()
  setup_zshrc()
  setup_aliases()


def setup_autosuggestions():
  plugin_path = expandvars('$HOME/.oh-my-zsh/custom/plugins/zsh-autosuggestions')
  if not isdir(plugin_path):
    run('git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions', shell=True, check=True)

def setup_aliases():
  alias_path = expandvars('$HOME/.oh-my-zsh/custom/aliases.zsh')
  if not isfile(alias_path):
    with open(alias_path, 'x') as alias_object:
      alias_object.write("""# Custom Aliases
# Shortcuts for zsh modifications
alias zshconfig="nvim $HOME/.zshrc"
alias ohmyzsh="nvim $HOME/.oh-my-zsh"
alias zshalias="nvim $HOME/.oh-my-zsh/custom/aliases.zsh"
alias zshsource="source $HOME/.zshrc"

# Alias for faster sudo edits
alias se="sudoedit"
alias sn="sudo -E nvim"

# some more ls aliases
alias ll='ls -al'
alias la='ls -Al'
""")


def setup_zsh_theme():
  zsh_theme_path = expandvars('$HOME/.oh-my-zsh/themes/headline')
  zsh_theme_link = expandvars('$HOME/.oh-my-zsh/themes/headline.zsh-theme')
  if not isdir(zsh_theme_path):
    print('Theme not found')
    run(f'git clone https://github.com/Moarram/headline.git {zsh_theme_path}', shell=True, check=True)
    run(f'ln -s {zsh_theme_path}/headline.zsh-theme {zsh_theme_link}', shell=True, check=True)


def setup_zshrc():
  zshrc_path = expandvars('$HOME/.zshrc')
  ohmyzsh_path = expandvars('$HOME/.oh-my-zsh')
  with open('zsh.json', 'r') as zsh_config_file:
    zsh_config = load(zsh_config_file)
  with open(zshrc_path, 'w' if isfile(zshrc_path) else 'x') as zshrc_object:
    zshrc_object.write(f"""# Custom Path Variables
export PATH=$HOME/.npm-global/bin:$HOME/.local/bin:$HOME/bin:/usr/.local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="{ohmyzsh_path}"

# Set name of the theme to load --- See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="headline"

# Uncomment the following line to change how often to auto-update (in days).
export UPDATE_ZSH_DAYS=7

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# Caution: this setting can cause issues with multiline prompts (zsh 5.7.1 and newer seem to work)
# See https://github.com/ohmyzsh/ohmyzsh/issues/5765
COMPLETION_WAITING_DOTS="true"


# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
DISABLE_UNTRACKED_FILES_DIRTY="true"

# Would you like to use another custom folder than $ZSH/custom?
ZSH_CUSTOM={ohmyzsh_path}/custom

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
plugins=({' '.join(zsh_config['plugins'])})

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='nvim'
fi

# Less should not paginate if less than a page
export LESS="-F -X $LESS"
""")


if __name__ == '__main__':
  install()
