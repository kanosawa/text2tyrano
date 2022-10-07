import regex


# 形態素に対してルビを振るクラス
#
# 連続した漢字群が形態素の中に１つだけという前提でルビを振る
class RubyMorpheme:
    def __init__(self):
        pass

    # ルビを振る
    def ruby(self, morpheme: str, hiragana: str) -> str:

        # 漢字群全体のふりがなを抽出
        kanji_start_idx = self.__find_kanji_start_idx(morpheme)
        if kanji_start_idx is None:
            return morpheme
        kanji_end_idx = self.__find_kanji_end_idx(morpheme, kanji_start_idx)
        kana = hiragana[kanji_start_idx: len(hiragana) - len(morpheme) + kanji_end_idx]

        morpheme_with_ruby = self.__make_morpheme_with_ruby(morpheme, kanji_start_idx, kanji_end_idx, kana)
        return morpheme_with_ruby

    # 形態素の文字列から漢字の始まりを探索する
    def __find_kanji_start_idx(self, morpheme: str) -> int:
        for i in range(len(morpheme)):
            if regex.match('^\p{Script=Han}+$', morpheme[i]) is not None:
                return i
        return None

    # 形態素の文字列から漢字の終わりを探索する
    def __find_kanji_end_idx(self, morpheme: str, start_idx: int) -> int:
        for i in range(start_idx + 1, len(morpheme)):
            if regex.match('^\p{Script=Han}+$', morpheme[i]) is None:
                return i
        return len(morpheme)

    # ルビ付きの形態素文字列を生成する
    def __make_morpheme_with_ruby(self, morpheme: str, kanji_start_idx: int, kanji_end_idx: int, kana: str) -> str:

        kanji_num = kanji_end_idx - kanji_start_idx
        ruby_length_for_one_kanji = len(kana) // kanji_num
        amari = len(kana) % kanji_num

        prev_ruby_idx = 0
        result = morpheme[:kanji_start_idx]
        for kanji_idx in range(kanji_num):
            current_ruby_idx = prev_ruby_idx + ruby_length_for_one_kanji
            if kanji_idx < amari:
                current_ruby_idx += 1
            result += '[ruby text="' + kana[prev_ruby_idx: current_ruby_idx] + '"]'
            result += morpheme[kanji_start_idx + kanji_idx]
            prev_ruby_idx = current_ruby_idx
        result += morpheme[kanji_end_idx:]

        return result
