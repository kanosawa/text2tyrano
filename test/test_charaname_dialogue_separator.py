import unittest

from charaname_dialogue_separator import CharanameDialogueSeparator


charaname_dialogue_separator = CharanameDialogueSeparator()


class CharanameDialogueSeparatorTestCase(unittest.TestCase):
    def test_empty_paragraph(self):
        paragraph = ''
        expected = (None, None)
        self.assertEqual(charaname_dialogue_separator.separate(paragraph), expected)

    def test_non_charaname_paragraph(self):
        paragraph = '「こんにちは」'
        expected = (None, None)
        self.assertEqual(charaname_dialogue_separator.separate(paragraph), expected)

    def test_charaname_and_dialogue_paragraph(self):
        paragraph = '#タマ「こんにちは」'
        expected = ('#タマ', '「こんにちは」')
        self.assertEqual(charaname_dialogue_separator.separate(paragraph), expected)

    def test_charaname_and_dialogue_paragraph2(self):
        paragraph = '#タマ『こんにちは』'
        expected = ('#タマ', '『こんにちは』')
        self.assertEqual(charaname_dialogue_separator.separate(paragraph), expected)

    def test_double_brackets_paragraph(self):
        paragraph = '#タマ「わたしは『タマ』だ」'
        expected = ('#タマ', '「わたしは『タマ』だ」')
        self.assertEqual(charaname_dialogue_separator.separate(paragraph), expected)


if __name__ == '__main__':
    unittest.main()
