vim-comment-box
===============
Create filetype-specific boxed comments.

Examples
--------

Create a boxed comment with `<leader>b` (or whatever mapping you set, see below).

```vim
set relativenumber
let example_var_one = "one"
let example_var_two = "two"

```

with cursor on the second line (and a textwidth of 31) will be changed to

```vim
set relativenumber
"""""""""""""""""""""""""""""""
" let example_var_one = "one" "
"""""""""""""""""""""""""""""""
let example_var_two = "two"
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
will result in (textwidth set to 80)

```html
<!DOCTYPE html>
<html>
    <!------------------------------------------------------------------------->
    <!--                                <head>                               -->
    <!--                        <meta charset="UTF-8">                       -->
    <!--                 <title>Title of the document</title>                -->
    <!--                               </head>                               -->
    <!------------------------------------------------------------------------->
    <body>
        Content of the document......
    </body>
</html> 
```

Prerequisites
-------------

- Your Vim was compiled with `+python` option (check by opening Vim and running 
  `:echo has('python')` - result needs to be `1`)

Installation
------------

Use your favorite plugin manager, e.g. [vim-plug](https://github.com/junegunn/vim-plug):

```vim
Plug 'pylipp/vim-comment-box'
```

After installation, create a custom keymapping in your `.vimrc` to call this plugin's only function. For example you could use the keymapping `<leader>b`:

```vim
nnoremap <leader>b :<C-u>call CommentBox()<CR>
```

Contributions
-------------

Missing support for your programming language of choice? Create an issue or a pull request :)

License
-------

Original idea by: Copyright (c) cbaumhardt. Distributed under the same terms as Vim itself (see `:help license`).

Fork by pylipp.

TODO
----

- format long lines
- different alignment options (center, ljust, rjust)
- undo option?
- test Python3 support
- handle error if filetype not supported
- handle lines that are already commented
- add optional space after text line comment char
