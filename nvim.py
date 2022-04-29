#!/bin/env python3
from subprocess import run
from os.path import isdir, isfile, expandvars
from os import makedirs


def setup_plugins():
  nvim_config_path = expandvars('$HOME/.config/nvim')
  nvim_config_file_path = f"{nvim_config_path}/init.vim"
  nvim_plug_path = expandvars('$HOME/.local/share/nvim/site/autoload')
  makedirs(nvim_plug_path, exist_ok=True)
  if not isfile(f"{nvim_plug_path}/plug.vim"):
    run(f"curl -fLo {nvim_plug_path}/plug.vim https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim", shell=True, check=True)
  makedirs(nvim_config_path, exist_ok=True)
  if not isfile(nvim_config_file_path):
    with open(nvim_config_file_path, 'x') as nvim_config_file:
      nvim_config_file.write("""" ###################
" # Loading Plugins #
" ###################

call plug#begin('~/.local/share/nvim/plugged')
" Load Plugins using:
" Plug 'github-directory/git url', { 'options': 'value' }
  Plug 'morhetz/gruvbox'
  Plug 'vim-airline/vim-airline'
  Plug 'vim-airline/vim-airline-themes'
  Plug 'tpope/vim-fugitive'
  Plug 'airblade/vim-gitgutter'
  Plug 'tpope/vim-surround'
  Plug 'scrooloose/nerdtree'
  Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
  Plug 'scrooloose/nerdcommenter'
  Plug 'ctrlpvim/ctrlp.vim'
  Plug 'majutsushi/tagbar'
  Plug 'neoclide/coc.nvim', {'branch': 'release'}
  Plug 'ryanoasis/vim-devicons' " Should be loaded last!
call plug#end()

" #########################
" # NeoVim Configurations #
" #########################

" Enable true color | Set encoding to utf8 | Enable filetype plugin
let $NVIM_TUI_ENABLE_TRUE_COLOR=1
set encoding=UTF-8
filetype plugin on

" Setting Tablength
set number
set relativenumber
let mapleader=','
set tabstop=2
set shiftwidth=2
set expandtab
set autoindent
syntax on
set hlsearch

" Enable vim-one theme and configure it
set background=light
let g:gruvbox_contrast_light='hard'
colorscheme gruvbox

" Start NERDTree. If a file is specified, move the cursor to its window.
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * NERDTree | if argc() > 0 || exists("s:std_in") | wincmd p | endif

" Exit Vim if NERDTree is the only window left.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() |
    \ quit | endif

" Fugitive Configuration
set statusline=%<%f\ %h%m%r%{FugitiveStatusline()}%=%-14.(%l,%c%V%)\ %P
let g:fugitive_no_maps = 1

" Adds a smart Tab line at the top with airline
let g:airline#extensions#tabline#enabled = 1

" NERDCommenter Config
" Create default mappings
let g:NERDCreateDefaultMappings = 1
" Align line-wise comment delimiters flush left instead of following code indentation
let g:NERDDefaultAlign = 'left'
" Add spaces after comment delimiters by default
let g:NERDSpaceDelims = 1
" Enable trimming of trailing whitespace when uncommenting
let g:NERDTrimTrailingWhitespace = 1

" Tagbar linenumbers
let g:tagbar_show_linenumbers = -1
let g:tagbar_show_tag_linenumbers = 1

" ############################
" # Code Completion settings #
" ############################
" Add :Prettier Command to vim
command! -nargs=0 Prettier :CocCommand prettier.formatFile

" ################
" # Key bindings #
" ################
nmap <F8> :TagbarToggle<CR> " Open Tagbar on F8

" Shortcuts for NERDTree
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>
""")
  run('nvim -c "PlugInstall|q|q"', shell=True)
  


def install():
  setup_plugins()


if __name__ == '__main__':
  install()
