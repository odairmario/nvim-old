# Nvim Configurations
## Plugin manger
First steps is configure de pluginr manager, we use the [vim plug](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links).
In linux can execute this line to install plugin manager:
```bash
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```

## My plugins
| Name     | Description        | Url                                                           |
|----------|--------------------|---------------------------------------------------------------|
| NerdTree | Tree file explorer | [scrooloose/nerdTree](https://github.com/preservim/nerdtree) |
|

## My configs
| Command                         | Description   | Note             |
|---------------------------------|---------------|------------------|
| `nmap <F4> NERDTreeToggle <CR>`{:.vim} | Open Nerdtree | Plugin: NERDTREE |
