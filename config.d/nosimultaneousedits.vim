" sempre seleciona a opção edit quando existe um arquivo de swap
augroup NoSimultaneousEdits
    autocmd!
    autocmd  SwapExists  *  :let v:swapchoice = 'e'
augroup END

