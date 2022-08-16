# Nvim Configurations
## Requirements
### Packages

```bash
pip install -r requirements.txt
```
### Plugin manger
First steps is configure de pluginr manager, we use the [vim plug](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links).
In linux can execute this line to install plugin manager:
```bash
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```
## How run
### NVIM:
To generate config do:
```bash
python3 nvim.py -o ~/.config/nvim/init.vim
```
To install plugins open `~/.config/nvim/init.vim` and do:
```bash
:PlugInstall
```
### VIM
To generate config do:
```bash
python3 nvim.py -o ~/.vimrc
```
To install plugins, open `~/.vimrc` and do `:PlugInstall`
### Notes:
After add new plugin on plugin table, need open vim config file and do `:PlugInstall`
## My plugins
| Name              | Description                               | Url                                                                                 |
|-------------------|-------------------------------------------|-------------------------------------------------------------------------------------|
| NerdTree          | Tree file explorer                        | [scrooloose/nerdTree](https://github.com/preservim/nerdtree)                        |
| CtrlP             | open buffers, files on vim with `<C-p>`   | [ctrlpvim/ctrlp.vim](https://github.com/ctrlpvim/ctrlp.vim )                        |
| Vim airline       | Airline bar                               | [bling/vim-airline](https://github.com/vim-airline/vim-airline)                     |
| Airline themes    | Themes for vim airline bar                | [vim-airline/vim-airline-themes](https://github.com/vim-airline/vim-airline-themes) |
| Deoplete          | Autocomplete Enginer                      | [Shougo/deoplete.nvim](https://github.com/Shougo/deoplete.nvim)                     |
| Deoplete-clangx   | Asynchronous C/C++ completion for Neovim. | [Shougo/deoplete-clangx](https://github.com/Shougo/deoplete-clangx)                 |
| deoplete-jedi     | python jedi completion                    | [deoplete-plugins/deoplete-jedi](https://github.com/deoplete-plugins/deoplete-jedi) |
| vim-table-mode    | vim table mode                            | [dhruvasagar/vim-table-mode](https://github.com/dhruvasagar/vim-table-mode)         |
| tagbar            | tagbar                                    | [majutsushi/tagbar](https://github.com/majutsushi/tagbar)                           |
| vim-snippets      | snniptes variados                         | [honza/vim-snippets](https://github.com/honza/vim-snippets)                         |
| ultisnips         | snniptes variados                         | [sirver/ultisnips](https://github.com/sirver/ultisnips)                             |
| NeoSolarized      | solarized coloscheme                      | [overcache/NeoSolarized](https://github.com/overcache/NeoSolarized)                 |
| Ale               | syntax checker                            | [dense-analysis/ale](https://github.com/dense-analysis/ale)                         |
| auto-pairs        | close pairs                               | [jiangmiao/auto-pairs](https://github.com/jiangmiao/auto-pairs)                     |
| GitGuTter         | git interface                             | [airblade/vim-gitgutter](https://github.com/airblade/vim-gitgutter)                 |
| spell-pt-br       | spell check ptbr                          | [mateusbraga/vim-spell-pt-br](https://github.com/mateusbraga/vim-spell-pt-br)       |
| tmux-complete.vim | tmux autocomplete                         | [wellle/tmux-complete.vim](https://github.com/wellle/tmux-complete.vim)             |
| saltstack plugin  | saltstack syntax                          | [saltstack/salt-vim](https://github.com/saltstack/salt-vim)                         |
| vim-nftables      | syntax for nftables                       | [nfnty/vim-nftables](https://github.com/nfnty/vim-nftables)                         |
| vim-jinja2-syntax | syntax for jinja template                 | [glench/vim-jinja2-syntax](https://github.com/glench/vim-jinja2-syntax)             |


## My configs
### General settings
| Command                                                     | Description                          |
|-------------------------------------------------------------|--------------------------------------|
| `syntax on`                                                 | Enable syntax highlight              |
| `set encoding=utf-8`                                        | set encoding to utf-8                |
| `set showmatch`                                             | briefly jump to matching brackets    |
| `set number`                                                | Show numbers                         |
| `set showcmd`                                               | show inserted command                |
| `set expandtab`                                             | tab 4 espaco                         |
| `set tabstop=4`                                             | tab 4 espaco                         |
| `set shiftwidth=4`                                          | tab 4 espaco                         |
| `set softtabstop=4`                                         | tab 4 espaco                         |
| `autocmd FileType html setlocal ts=2 sts=2 sw=2`            | html file with 2 spaces              |
| `autocmd FileType sls setlocal ft=yaml`                     | sls file with 2 spaces               |
| `autocmd FileType plaintex set ft=tex tw=100 spell`         | tex file with 2 spaces               |
| `autocmd FileType tex set  tw=100 spell`                    | tex file with 2 spaces               |
| `autocmd FileType tex setlocal ts=2 sts=2 sw=2 `            | tex file with 2 spaces               |
| `autocmd FileType typescriptreact setlocal ts=2 sts=2 sw=2` | typescript react  with 2 spaces      |
| `autocmd FileType tsx setlocal ts=2 sts=2 sw=2`             | typescript with 2 spaces             |
| `set ruler`                                                 | enable ruler                         |
| `set hls`                                                   | enable highlights on search patterns |
| `set ai`                                                    | enable auto ident                    |
| `set aw`                                                    | enable auto saving on switch buffer  |
| `set viminfo=%,'50,\"100,/100,:100,n`                       | storage buffer options               |
| `nmap <C-Down> ddp`                                         | move line to down                    |
| `nmap <C-Up> ddkP`                                          | move line to up                      |
| `nmap cc diwi`                                              | cut word and enter to insertmode     |
| `nmap <F1> :NERDTree <CR>`                                  | NERDTree shotcut                     |
| `nmap <F2> :noh <CR>`                                       | disable highlight                    |
| `nmap <F4> :NERDTreeToggle <CR>`                            | toggle NERDTree                      |
| `nmap <F3> :TagbarOpenAutoClose <CR>`                       | toggle TagBar                        |
| `set showbreak=+++`                                         | wrap-broken line prefix              |
| `set cindent "indent estilo c`                              | indent style c                       |
| `set nowrap`                                                | dont break lines                     |
| `set spelllang=pt_br,en`                                    | spell check                          |
| `set mouse=ci`                                              | funcoes mouse                        |
| `let mapleader=" "`                                         | map leader to space                  |
| `noremap <Leader>y "*y`                                     | copy to clipboard                    |
| `noremap <Leader>p "*p`                                     | paste from clipboard                 |
| `noremap <Leader>Y "+y`                                     | copy to clipboard                    |
| `noremap <Leader>P "+p`                                     | paste clipboard                      |
| `set backup`                                                | enable backup                        |
| `set backupdir=~/.nvim/backup/ `                            | backupdir                            |
| `set directory=~/.nvim/swap/ `                              | swap dir                             |
| `set undodir=~/.nvim/undo/ `                                | undo dir                             |
| `set undofile`                                              | save undofile                        |
| `set background=dark`                                       | set the background color to dark     |
#### Details
The backup configs presume the directories are created, if not then run:
```
mkdir ~/.nvim/{backup,undo,swap}
```
### Plugins settings
| Command                                               | Description                       | Plugin        |
|-------------------------------------------------------|-----------------------------------|---------------|
| `nmap <F4> NERDTreeToggle <CR>`                       | Open Nerdtree                     | NERDTREE      |
| `let g:deoplete#enable_at_startup = 1`                | Enable deoplete on startup        | Deoplete      |
| `autocmd FileType md  :silent :TableModeEnable`       | enable TableMode to markdown file | vim-markdown  |
| `autocmd FileType markdown  :silent :TableModeEnable` | enable TableMode to markdown file | vim-markdown  |
| `let g:UltiSnipsExpandTrigger="<c-j>"`                | enable snippets                   | utils-snips   |
| `let g:UltiSnipsJumpForwardTrigger="<c-b>"`           |                                   | utils-snips   |
| `let g:UltiSnipsJumpBackwardTrigger="<c-z>"`          |                                   | utils-snips   |
| `let g:ale_completion_enabled = 1`                    | enable ale completion             | ale           |
| `let g:ale_completion_autoimport = 1`                 | ale completion autoimport         | ale           |
| `let g:ale_fix_on_save = 1`                           | fix on save                       | ale           |
| `let g:airline#extensions#ale#enabled = 1`            | intregate ale with airline bar    | ale           |
| `colorscheme NeoSolarized`                            | neo solarized                     | neosolarized  |
| `let g:tmuxcomplete#trigger = ''`                     | deoplete dont need trigger        | tmux-complete |
# void
