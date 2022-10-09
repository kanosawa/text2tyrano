import re
from typing import List


# 段落を改行するクラス
#
# 句点で改行後、読点で改行。
# todo: 読点ではない場所で改行した方がよいケースに対応
class LineBreaker:
    def __init__(self, max_line_num, appropriate_max_chara_num):
        self.max_line_num = max_line_num  # 最大行数
        self.appropriate_max_chara_num = appropriate_max_chara_num  # 一行の適切な最大文字数

    # 改行する
    def break_line(self, paragraph: str) -> List[str]:
        result_lines = self.separate_by_period(paragraph)
        while True:
            longest_sentense_idx = result_lines.index(max(result_lines, key=len))
            max_sentense_length = len(result_lines[longest_sentense_idx])
            if len(result_lines) >= self.max_line_num or max_sentense_length <= self.appropriate_max_chara_num:
                break
            new_lines = self.break_by_comma(result_lines[longest_sentense_idx])
            del result_lines[longest_sentense_idx]
            for i, new_line in enumerate(new_lines):
                result_lines.insert(longest_sentense_idx + i, new_line)
        return result_lines

    # 段落を句点で分割する
    def separate_by_period(self, paragraph: str) -> List[str]:
        spans = [match.span() for match in re.finditer('。', paragraph)]
        sentenses = []
        prev_pos = 0
        for span in spans:
            sentenses.append(paragraph[prev_pos:span[1]])
            prev_pos = span[1]
        length = len(paragraph)
        if prev_pos < length:
            sentenses.append(paragraph[prev_pos:])
        return sentenses

    # 処理後の２文ができるだけ同じ長さになるよう読点で改行する
    def break_by_comma(self, sentense: str) -> List[str]:
        spans = [match.span() for match in re.finditer('、', sentense)]
        half_nearest_idx = spans.index(min(spans, key=lambda x: abs(len(sentense) / 2 - x[1])))
        break_pos = spans[half_nearest_idx][1]
        return [sentense[:break_pos], sentense[break_pos:]]
