import unittest

from paragraph_separator import ParagraphSeparator


paragraph_separator = ParagraphSeparator(3, 32)


class ParagraphSeparatorTestCase(unittest.TestCase):
    def test_one_paragraph(self):
        paragraph = '今まではお姉ちゃんとか、子どもの先生なんてからかわれて呼ばれていたから、初めて名前を憶えられたということが、すっごく嬉しかった。'
        expected = ['今まではお姉ちゃんとか、子どもの先生なんてからかわれて呼ばれていたから、初めて名前を憶えられたということが、すっごく嬉しかった。']
        self.assertEqual(paragraph_separator.separate(paragraph), expected)

    def test_three_short_paragraph(self):
        paragraph = '子どもの先生なんてからかわれて呼ばれていたから。初めて名前を憶えられたということが。すっごく嬉しかった。'
        expected = ['子どもの先生なんてからかわれて呼ばれていたから。初めて名前を憶えられたということが。すっごく嬉しかった。']
        self.assertEqual(paragraph_separator.separate(paragraph), expected)

    def test_three_long_paragraph(self):
        paragraph = '今まではお姉ちゃんとか、子どもの先生なんてからかわれて呼ばれていたから。初めて名前を憶えられたということが。すっごく嬉しかった。'
        expected = ['今まではお姉ちゃんとか、子どもの先生なんてからかわれて呼ばれていたから。', '初めて名前を憶えられたということが。すっごく嬉しかった。']
        self.assertEqual(paragraph_separator.separate(paragraph), expected)

    def test_four_short_paragraph(self):
        paragraph = 'あ。あ。あ。あ。'
        expected = ['あ。あ。', 'あ。あ。']
        self.assertEqual(paragraph_separator.separate(paragraph), expected)

    def test_one_paragraph_without_period(self):
        paragraph = '今まではお姉ちゃんとか、子どもの先生なんてからかわれて呼ばれていたから、初めて名前を憶えられたということが、すっごく嬉しかった'
        expected = ['今まではお姉ちゃんとか、子どもの先生なんてからかわれて呼ばれていたから、初めて名前を憶えられたということが、すっごく嬉しかった']
        self.assertEqual(paragraph_separator.separate(paragraph), expected)

    def test_three_short_paragraph_without_period(self):
        paragraph = '子どもの先生なんてからかわれて呼ばれていたから。初めて名前を憶えられたということが。すっごく嬉しかった'
        expected = ['子どもの先生なんてからかわれて呼ばれていたから。初めて名前を憶えられたということが。すっごく嬉しかった']
        self.assertEqual(paragraph_separator.separate(paragraph), expected)

    def test_three_long_paragraph_without_period(self):
        paragraph = '今まではお姉ちゃんとか、子どもの先生なんてからかわれて呼ばれていたから。初めて名前を憶えられたということが。すっごく嬉しかった'
        expected = ['今まではお姉ちゃんとか、子どもの先生なんてからかわれて呼ばれていたから。', '初めて名前を憶えられたということが。すっごく嬉しかった']
        self.assertEqual(paragraph_separator.separate(paragraph), expected)

    def test_four_short_paragraph_without_period(self):
        paragraph = 'あ。あ。あ。あ'
        expected = ['あ。あ。', 'あ。あ']
        self.assertEqual(paragraph_separator.separate(paragraph), expected)


if __name__ == '__main__':
    unittest.main()
