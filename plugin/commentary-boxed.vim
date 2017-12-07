" https://github.com/cbaumhardt/vim-commentary-boxed
" extends tpope's vim-commentary plugin to create boxed elements
" see github pages for all information regarding vim-commentary-boxed

let g:plugin_path = expand('<sfile>:p:h')

function! ToggleBox()
  if has('python')
    if !exists("*PythonToggleBox")
      function PythonToggleBox()
python << EOF
import vim
import os
import sys

# https://robertbasic.com/blog/import-custom-python-modules-in-vim-plugins/
plugin_path = vim.eval("g:plugin_path")
python_module_path = os.path.abspath(os.path.join(plugin_path, "..", "lib"))
sys.path.append(python_module_path)
from commentbox import put_text_in_box

prefix = int(vim.eval('v:count1'))
this_buffer = vim.current.buffer
(row,col) = vim.current.window.cursor # row is 1 for first line
initial_number_of_lines = len(this_buffer)

current_line = vim.current.line
text_width = int(vim.eval("&tw"))
first_line, text_line, last_line = put_text_in_box(current_line, text_width)
this_buffer.append(last_line, row)
this_buffer.append(first_line, row - 1)
this_buffer[row] = text_line

def get_comment_information():
    # create a test line (9 chars) at the buffer end and comment it out
    this_buffer.append('test line', initial_number_of_lines - 1)
    vim.command(':' + str(initial_number_of_lines + 1) + 'Commentary')
    # determine comment_start_str (e.g. '<!--' for html) and calulate how
    # many free chars fit into a line (e.g. 80 - len('<!--  -->') = 71
    global comment_start_str, number_free_chars
    commented_line = this_buffer[initial_number_of_lines]
    comment_start_str = commented_line.split()[0]
    number_free_chars = 80 - (len(commented_line) - 9)
    del this_buffer[initial_number_of_lines] # delete test line again

def if_boxed_get_line_numbers_of_box_start_and_end():
    if not vim.current.line.startswith(comment_start_str + ' '):
        return None # not a comment, hence not part of a box
    # line was a comment, but not necessarily a box
    box_border = comment_start_str + ' ' + '-' * number_free_chars
    # determine whether there is a border line above
    row_border_above = None
    for i in range(1,row):
        vim.current.window.cursor = (row - i, col) # move 1 up
        if not vim.current.line.startswith(comment_start_str + ' '):
            break
        elif vim.current.line.startswith(box_border):
            (row_border_above, col_) = vim.current.window.cursor
            break
    # determine whether there is a border line below
    row_border_below = None
    for i in range(row + 1, initial_number_of_lines + 1):
        vim.current.window.cursor = (i, col) # move 1 down
        if not vim.current.line.startswith(comment_start_str + ' '):
            break
        elif vim.current.line.startswith(box_border):
            (row_border_below, col_) = vim.current.window.cursor
            break
    vim.current.window.cursor = (row, col) # reset to initial line
    if vim.current.line.startswith(box_border):
        # either the other box_border is above or below (or nowhere)
        if row_border_above is not None:
            if row - row_border_above == 1: # no box if middle part missing
                row_border_above = None
        if row_border_below is not None:
            if row_border_below - row == 1: # no box if middle part missing
                row_border_below = None
        # return for the case that the initial line was a box_border
        if row_border_above is not None or row_border_below is not None:
            if row_border_above is not None:
                return (row_border_above, row)
            else:
                return (row, row_border_below)
        else:
            return None
    else: # line is a comment, but not one with a box_border
        if row_border_above is not None and row_border_below is not None:
            return (row_border_above, row_border_below)
        else:
            return None

def box_lines(row, prefix): # box will contain line(s) starting at row
    if row + prefix - 1 > initial_number_of_lines: # special case at file end
        prefix = initial_number_of_lines - row + 1
    if row <= 1: # insert line at beginning, as buf.append() function can't do it
        this_buffer[0:0] = ['-' * number_free_chars]
    else:
        this_buffer.append('-' * number_free_chars, row - 2)
    this_buffer.append('-' * number_free_chars, row - 1 + prefix)
    vim.command(':' + str(row) + ',' + str(row + 1 + prefix) + 'Commentary')
    # handle special case that comments on empty strings don't work
    for i in range(prefix):
        line = this_buffer[row + i]
        if line.strip() == '':
            this_buffer[row + i] = comment_start_str + ' ' + line
    vim.current.window.cursor = (row + 1, col + len(comment_start_str) + 1)

# get_comment_information()
# result = if_boxed_get_line_numbers_of_box_start_and_end()
result = None
if result is not None: # unbox
    (box_begins_at, box_ends_at) = result
    vim.command(':' + str(box_begins_at) + ',' + str(box_ends_at) + 'Commentary')
    del this_buffer[box_ends_at - 1]
    del this_buffer[box_begins_at - 1]
    (cur_row, cur_col) = vim.current.window.cursor
    vim.current.window.cursor = (cur_row, 0)
    if box_ends_at - cur_row - 1 == 0: # unboxing at bottom border
        vim.current.window.cursor = (cur_row - 1, 0)
else: # box line(s)
    # box_lines(row, prefix)
    pass
EOF
      endfunction
    endif
    call PythonToggleBox()
  elseif !has('python')
    echom 'This function will not work, no +python support detected'
  else
    echom 'Could not detect plugin tpope/vim-commentary.'
    echom 'Please install and activate vim-commentary to use this function.'
  endif
endfunction
