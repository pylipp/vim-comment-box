" https://github.com/pylipp/vim-commentary-boxed
" Create filetype-specific comment box around current line

let g:plugin_path = expand('<sfile>:p:h')

function! CommentBox() abort
  if has('python')
    if !exists("*PythonCommentBox")
      function PythonCommentBox()
python << EOF
import vim
import os
import sys

# https://robertbasic.com/blog/import-custom-python-modules-in-vim-plugins/
plugin_path = vim.eval("g:plugin_path")
python_module_path = os.path.abspath(os.path.join(plugin_path, "..", "lib"))
sys.path.append(python_module_path)
from commentbox import put_text_in_box

count = int(vim.eval('v:count1'))
row, _ = vim.current.window.cursor  # row is 1 for first line
text_width = int(vim.eval("&tw"))
filetype = vim.eval("&ft")

put_text_in_box(vim.current.buffer, row, text_width, count=count,
                filetype=filetype)
EOF
      endfunction
    endif
    call PythonCommentBox()
  else
    echom 'This function will not work, no +python support detected'
  endif
endfunction
