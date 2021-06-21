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

## My plugins
| Name            | Description                               | Url                                                                                 |
|-----------------|-------------------------------------------|-------------------------------------------------------------------------------------|
| NerdTree        | Tree file explorer                        | [scrooloose/nerdTree](https://github.com/preservim/nerdtree)                        |
| CtrlP           | open buffers, files on vim with `<C-p>`   | [ctrlpvim/ctrlp.vim](https://github.com/ctrlpvim/ctrlp.vim )                        |
| Vim airline     | Airline bar                               | [bling/vim-airline](https://github.com/vim-airline/vim-airline)                     |
| Airline themes  | Themes for vim airline bar                | [vim-airline/vim-airline-themes](https://github.com/vim-airline/vim-airline-themes) |
| Deoplete        | Autocomplete Enginer                      | [Shougo/deoplete.nvim](https://github.com/Shougo/deoplete.nvim)                     |
| Deoplete-clangx | Asynchronous C/C++ completion for Neovim. | [Shougo/deoplete-clangx](https://github.com/Shougo/deoplete-clangx)                 |

## My configs
### General settings 
| Command                                          | Description                          |
|--------------------------------------------------|--------------------------------------|
| `syntax on`                                      | Enable syntax highlight              |
| `set encoding=utf-8`                             | set encoding to utf-8                |
| `set showmatch`                                  | briefly jump to matching brackets    |
| `set textwidth=90`                               | text width                           |
| `set number`                                     | Show numbers                         |
| `set showcmd`                                    | show inserted command                |
| `set expandtab`                                  | tab 4 espaco                         |
| `set tabstop=4`                                  | tab 4 espaco                         |
| `set shiftwidth=4`                               | tab 4 espaco                         |
| `set softtabstop=4`                              | tab 4 espaco                         |
| `autocmd FileType html setlocal ts=2 sts=2 sw=2` | html file with 2 spaces              |
| `autocmd FileType sls setlocal ft=yaml`          | sls file with 2 spaces               |
| `autocmd FileType tex setlocal ts=2 sts=2 sw=2`  | tex file with 2 spaces               |
| `set ruler`                                      | enable ruler                         |
| `set hls`                                        | enable highlights on search patterns |
| `set ai`                                         | enable auto ident                    |
| `set aw`                                         | enable auto saving on switch buffer  |
| `set columns=100`                                | window with 100 columns              |
| `set viminfo=%,'50,\"100,/100,:100,n`            | storage buffer options               |
| `nmap <C-Down> ddp`                              | move line to down                    |
| `nmap <C-Up> ddkP`                               | move line to up                      |
| `nmap cc diwi`                                   | cut word and enter to insertmode     |
| `nmap <F1> :make! <CR>`                          | make shotcut                         |
| `nmap <F2> :noh <CR>`                            | disable highlight                    |
| `nmap <F4> :NERDTreeToggle <CR>`                  | toggle NERDTree                      |
| `nmap <F3> :TagbarOpenAutoClose <CR>`            | toggle TagBar                        |
| `set showbreak=+++	" Wrap-broken line prefix`   | wrap-broken line prefix              |
| `set cindent "indent estilo c`                   | indent style c                       |

### Plugins settings
| Command                                               | Description                       | Plugin       |
|-------------------------------------------------------|-----------------------------------|--------------|
| `nmap <F4> NERDTreeToggle <CR>`                       | Open Nerdtree                     | NERDTREE     |
| `let g:deoplete#enable_at_startup = 1`                | Enable deoplete on startup        | Deoplete     |
| `autocmd FileType md  :silent :TableModeEnable`       | enable TableMode to markdown file | vim-markdown |
| `autocmd FileType markdown  :silent :TableModeEnable` | enable TableMode to markdown file | vim-markdown |

