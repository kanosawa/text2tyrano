import unittest

from ruby_morpheme import RubyMorpheme


ruby_morpheme = RubyMorpheme()


class RubyMorphemeTestCase(unittest.TestCase):
    def test_empty_morpheme(self):
        morpheme = ''
        hiragana = ''
        expected = ''
        self.assertEqual(ruby_morpheme.ruby(morpheme, hiragana), expected)

    def test_kana_morpheme(self):
        morpheme = 'こんにちは'
        hiragana = 'こんにちは'
        expected = 'こんにちは'
        self.assertEqual(ruby_morpheme.ruby(morpheme, hiragana), expected)

    def test_one_kanji_only_morpheme(self):
        morpheme = '一'
        hiragana = 'いち'
        expected = '[ruby text="いち"]一'
        self.assertEqual(ruby_morpheme.ruby(morpheme, hiragana), expected)

    def test_two_kanji_only_morpheme(self):
        morpheme = '一二'
        hiragana = 'いちに'
        expected = '[ruby text="いち"]一[ruby text="に"]二'
        self.assertEqual(ruby_morpheme.ruby(morpheme, hiragana), expected)

    def test_kanji_and_kana_morpheme(self):
        morpheme = 'あ一二い'
        hiragana = 'あいちにい'
        expected = 'あ[ruby text="いち"]一[ruby text="に"]二い'
        self.assertEqual(ruby_morpheme.ruby(morpheme, hiragana), expected)


if __name__ == '__main__':
    unittest.main()
