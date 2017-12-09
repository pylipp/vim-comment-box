"""Definition of filetype-specific comment characters."""


class CommentChars(object):
    def __init__(self, start, end=None, fill=None):
        self.start = start
        self.end = end or start
        self.fill = fill or start

    @property
    def size(self):
        return len(self.start) + len(self.end)


class PythonCommentChars(CommentChars):
    def __init__(self):
        super(PythonCommentChars, self).__init__('#')


class CCommentChars(CommentChars):
    def __init__(self):
        super(CCommentChars, self).__init__('/*', '*/', '*')


class VimCommentChars(CommentChars):
    def __init__(self):
        super(VimCommentChars, self).__init__('"')


class HtmlCommentChars(CommentChars):
    def __init__(self):
        super(HtmlCommentChars, self).__init__('<!--', '-->', '-')


SUPPORTED_COMMENT_CHARS = {
    "python": PythonCommentChars,
    "c": CCommentChars,
    "cpp": CCommentChars,
    "java": CCommentChars,
    "vim": VimCommentChars,
    "sh": PythonCommentChars,
    "html": HtmlCommentChars,
    "xml": HtmlCommentChars,
}


def get_comment_chars(filetype):
    return SUPPORTED_COMMENT_CHARS[filetype]()
