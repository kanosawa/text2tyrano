import re
import pykakasi
from typing import List


# 段落を改行するクラス
#
# 。！？、読点、形態素で改行。
class LineBreaker:
    def __init__(self, max_line_num, appropriate_max_chara_num):
        self.max_line_num = max_line_num  # 最大行数
        self.appropriate_max_chara_num = appropriate_max_chara_num  # 一行の適切な最大文字数
        self.kks = pykakasi.kakasi()

    # 改行する
    def break_line(self, paragraph: str) -> List[str]:
        result_lines = self.separate_by_period_exclamation_question(paragraph)

        while len(result_lines) > 0:

            longest_sentense_idx = result_lines.index(max(result_lines, key=len))
            max_sentense_length = len(result_lines[longest_sentense_idx])
            if len(result_lines) >= self.max_line_num or max_sentense_length <= self.appropriate_max_chara_num:
                break

            new_lines = self.break_by_comma(result_lines[longest_sentense_idx])
            if len(new_lines) == 0:
                new_lines = self.break_by_morpheme(result_lines[longest_sentense_idx])

            del result_lines[longest_sentense_idx]
            for i, new_line in enumerate(new_lines):
                result_lines.insert(longest_sentense_idx + i, new_line)

        return result_lines

    # 段落を。！？で分割する
    def separate_by_period_exclamation_question(self, paragraph: str) -> List[str]:

        # とりあえず全部の。！？で分割
        spans = [match.span() for match in re.finditer('[。？！]', paragraph)]
        sentenses = []
        prev_pos = 0
        for span in spans:
            sentenses.append(paragraph[prev_pos:span[1]])
            prev_pos = span[1]
        length = len(paragraph)
        if prev_pos < length:
            sentenses.append(paragraph[prev_pos:])

        # 前後の行を再結合してもappropriate_max_chara_numより短いなら再結合
        while True:
            out_from_while = True
            for i in range(len(sentenses) - 1):
                former = sentenses[i]
                latter = sentenses[i + 1]
                if len(former) + len(latter) < self.appropriate_max_chara_num:
                    del sentenses[i + 1]
                    del sentenses[i]
                    sentenses.insert(i, former + latter)
                    out_from_while = False
                    break
            if out_from_while:
                break

        return sentenses

    # 処理後の２文ができるだけ同じ長さになるよう"読点"で改行する
    def break_by_comma(self, sentense: str) -> List[str]:
        spans = [match.span() for match in re.finditer('、', sentense)]
        if len(spans) == 0:
            return []
        half_nearest_idx = spans.index(min(spans, key=lambda x: abs(len(sentense) / 2 - x[1])))
        break_pos = spans[half_nearest_idx][1]
        return [sentense[:break_pos], sentense[break_pos:]]

    # 処理後の２文ができるだけ同じ長さになるよう"形態素"で改行する
    def break_by_morpheme(self, sentense: str) -> List[str]:
        converted_list = self.kks.convert(sentense)
        length_list = list(map(lambda x: len(x['orig']), converted_list))
        pos_list = []
        prev_pos = 0
        for length in length_list:
            current_pos = prev_pos + length
            pos_list.append(current_pos)
            prev_pos = current_pos
        half_nearest_idx = pos_list.index(min(pos_list, key=lambda x: abs(len(sentense) / 2 - x)))

        def make_separated_line(start, end):
            line = ''
            for morpheme in converted_list[start: end]:
                line += morpheme['orig']
            return line

        return [make_separated_line(0, half_nearest_idx + 1), make_separated_line(half_nearest_idx + 1, len(converted_list))]


def main():
    line_Braker = LineBreaker(3, 32)
    paragraph = '今まではお姉ちゃんとか、子どもの先生なんてからかわれて呼ばれていたから、初めて名前を憶えられたということが、すっごく嬉しかった。'
    result = line_Braker.break_line(paragraph)
    print("\n変換前")
    print(paragraph)
    print("\n変換後")
    for r in result:
        print(r)


if __name__ == '__main__':
    main()
