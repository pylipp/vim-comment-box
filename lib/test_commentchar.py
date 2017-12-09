import unittest

from commentchar import PythonCommentChars, CCommentChars, get_comment_chars,\
    HtmlCommentChars


class TestCommentChars(unittest.TestCase):
    def test_python(self):
        self.assertEqual(PythonCommentChars().size, 2)

    def test_c(self):
        self.assertEqual(CCommentChars().size, 4)

    def test_html(self):
        self.assertEqual(HtmlCommentChars().size, 7)

    def test_get_comment_char(self):
        chars = get_comment_chars("sh")
        self.assertEqual(chars.size, 2)

    def test_get_comment_char_fail(self):
        self.assertRaises(KeyError, get_comment_chars, "perl")


if __name__ == "__main__":
    unittest.main()
