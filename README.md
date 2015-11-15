vim-commentary-boxed
====================
Extend [tpope's vim-commentary](https://github.com/tpope/vim-commentary) 
plugin to create boxed comments. 

Examples
--------

Create a boxed comment with `<leader>b` (or whatever mapping you set, see below).

```vim
set relativenumber
let example_var_one = "one"
let example_var_two = "two"

```

with cursor on the second line will be changed to

```vim
set relativenumber
" ##############################################################################
" let example_var_one = "one"
" ##############################################################################
let example_var_two = "two"

```
Calling `<leader>b` from the empty row on the bottom will result in 

```vim
set relativenumber
let example_var_one = "one"
let example_var_two = "two"
" ##############################################################################
" 
" ##############################################################################
```
The commenting string will automatically adapt to the respective buffer filetype.
Note that you can give this plugin a count, too. Calling `4<leader>b` from line
3 of

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Title of the document</title>
    </head>
    <body>
        Content of the document......
    </body>
</html> 
```
will result in

```html
<!DOCTYPE html>
<html>
<!-- ####################################################################### -->
<!--     <head> -->
<!--         <meta charset="UTF-8"> -->
<!--         <title>Title of the document</title> -->
<!--     </head> -->
<!-- ####################################################################### -->
    <body>
        Content of the document......
    </body>
</html> 
```

To delete a comment box, place the cursor on any line of the box and type
`<leader>b`.

Prerequisites
-------------

- You have installed the [vim-commentary](https://github.com/tpope/vim-commentary) 
  plugin and it is active
- Your Vim was compiled with `+python` option (check by opening Vim and running 
  `:echo has('python')` - result needs to be `1`)

Installation
------------

Use your favorite plugin manager, e.g. [vim-plug](https://github.com/junegunn/vim-plug):

```vim
Plug 'cbaumhardt/vim-commentary-boxed'
```

After installation, create a custom keymapping in your `.vimrc` to call this plugin's only function. For example you could use the keymapping `<leader>b`:

```vim
nnoremap <leader>b :<C-u>call ToggleBox()<CR>
```

License
-------

Copyright (c) cbaumhardt. Distributed under the same terms as Vim itself (see `:help license`).
