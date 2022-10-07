import unittest

from kanji_grade_calculator import KanjiGradeCalculator


kanji_grade_calculator = KanjiGradeCalculator('../joyo2010.txt')


class KanjiGradeCalculatorTestCase(unittest.TestCase):
    def test_empty_paragraph(self):
        str_in = ''
        expected = 0
        self.assertEqual(kanji_grade_calculator.calculate(str_in), expected)

    def test_kana_paragraph(self):
        str_in = 'おはようオヤスミ'
        expected = 0
        self.assertEqual(kanji_grade_calculator.calculate(str_in), expected)

    def test_common_paragraph(self):
        str_in = '鬱病'
        expected = 7
        self.assertEqual(kanji_grade_calculator.calculate(str_in), expected)

    def test_uncommon_paragraph(self):
        str_in = '躁鬱病'
        expected = 8
        self.assertEqual(kanji_grade_calculator.calculate(str_in), expected)


if __name__ == '__main__':
    unittest.main()
