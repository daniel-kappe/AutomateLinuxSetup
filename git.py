#!/bin/env python3
from os.path import isfile, expandvars
from json import load

def configure():
  write_gitconfig()
  write_ignore()
  write_message()


def write_message():
  message_path = expandvars('$HOME/.gitmessage')
  if not isfile(message_path):
    with open(message_path, 'x') as message_file:
      message_file.write("""Subject line (< 50 characters) imperative wording

Body for detailed description. Keep lines shorter than 72 characters
and give answer to the questions: what changed and why?

[Ticket|Issue|Reference: XXX]""")


def write_ignore():
  ignore_path = expandvars('$HOME/.gitignore_global')
  if not isfile(ignore_path):
    with open(ignore_path, 'x') as ignore_file:
      ignore_file.write("""# JetBrains Editors
.idea/

# GPG
secring.*

# VSCode
.vscode/
.history/
*.vsix""")

def write_gitconfig():
  config_path = expandvars('$HOME/.gitconfig')
  with open('git.json', 'r') as git_config:
    config = load(git_config)
  if not isfile(config_path):
    with open(config_path, 'x') as config_file:
      config_file.write(f"""[core]
editor = nvim
excludefile = ~/.gitignore_global
autocrlf = input
[commit]
template = ~/.gitmessage
[user]
email = {config["email"]}
name = {config["name"]}
signingkey = {config["signingkey"]}
[color]
ui = true
[alias]
dfs = diff --staged
logg = log --graph --decorate --oneline --all
praise = blame
amend = commit --amend
unstage = restore --staged
[init]
defaultBranch = main""")


if __name__ == '__main__':
  configure()

