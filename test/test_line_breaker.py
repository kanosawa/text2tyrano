import unittest

from line_breaker import LineBreaker


line_breaker = LineBreaker(3, 20)


class LineBreakerTestCase(unittest.TestCase):
    def test_one_paragraph(self):
        paragraph = '今まではお姉ちゃんとか、子どもの先生なんてからかわれて呼ばれていたから、初めて名前を憶えられたということが、すっごく嬉しかった。'
        expected = ['今まではお姉ちゃんとか、', '子どもの先生なんてからかわれて呼ばれていたから、', '初めて名前を憶えられたということが、すっごく嬉しかった。']
        self.assertEqual(line_breaker.break_line(paragraph), expected)

    def test_three_short_paragraph(self):
        paragraph = '子どもの先生なんてからかわれて呼ばれていたから。初めて名前を憶えられたということが。すっごく嬉しかった。'
        expected = ['子どもの先生なんてからかわれて呼ばれていたから。', '初めて名前を憶えられたということが。', 'すっごく嬉しかった。']
        self.assertEqual(line_breaker.break_line(paragraph), expected)

    def test_three_long_paragraph(self):
        paragraph = '今まではお姉ちゃんとか、子どもの先生なんてからかわれて呼ばれていたから。初めて名前を憶えられたということが。すっごく嬉しかった。'
        expected = ['今まではお姉ちゃんとか、子どもの先生なんてからかわれて呼ばれていたから。', '初めて名前を憶えられたということが。', 'すっごく嬉しかった。']
        self.assertEqual(line_breaker.break_line(paragraph), expected)

    def test_one_paragraph_without_period(self):
        paragraph = '今まではお姉ちゃんとか、子どもの先生なんてからかわれて呼ばれていたから、初めて名前を憶えられたということが、すっごく嬉しかった'
        expected = ['今まではお姉ちゃんとか、', '子どもの先生なんてからかわれて呼ばれていたから、', '初めて名前を憶えられたということが、すっごく嬉しかった']
        self.assertEqual(line_breaker.break_line(paragraph), expected)

    def test_two_short_paragraph(self):
        paragraph = 'こんにちは。さようなら'
        expected = ['こんにちは。さようなら']
        self.assertEqual(line_breaker.break_line(paragraph), expected)

    def test_question_paragraph(self):
        paragraph = '子どもの先生なんてからかわれて呼ばれていたから？　初めて名前を憶えられたということが。すっごく嬉しかった。'
        expected = ['子どもの先生なんてからかわれて呼ばれていたから？', '　初めて名前を憶えられたということが。', 'すっごく嬉しかった。']
        self.assertEqual(line_breaker.break_line(paragraph), expected)


if __name__ == '__main__':
    unittest.main()
