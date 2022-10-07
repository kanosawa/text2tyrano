import re
import numpy as np
import math
from typing import List, Tuple


# 段落を分割するためのクラス
#
# １つの段落を入力し、必要があれば２つに分割し、リストとして出力する。
# 分割の必要がなければ、入力した１つの段落のみを要素とするリストを出力する。
# todo: ３つ以上の段落に分割できるようにする, 一行が複数の短文で構成される可能性を考慮できるようにする
class ParagraphSeparator:
    def __init__(self, max_line_num: int, max_chara_num_in_line: int):
        self.max_line_num = max_line_num  # 最大行数
        self.max_chara_num_in_line = max_chara_num_in_line  # 一行の最大文字数

    # パラグラフを分割する
    def separate(self, paragraph: str) -> List[str]:
        spans = [match.span() for match in re.finditer('。', paragraph)]
        if self.is_one_sentence(paragraph, spans) or self.is_less_than_max_line_num(paragraph, spans):
            return [paragraph]
        return self.separate_to_two_paragraph(paragraph, spans)

    # 一行かどうか
    def is_one_sentence(self, paragraph: str, spans: List[Tuple[int, int]]) -> bool:
        return len(spans) == 0 or spans[0][1] == len(paragraph)

    # 最大行数以内か
    def is_less_than_max_line_num(self, paragraph: str, spans: List[Tuple[int, int]]) -> bool:
        return self.calc_line_num(paragraph, spans) <= self.max_line_num

    # 段落をできるだけ均等になるように二分割する
    def separate_to_two_paragraph(self, paragraph: str, spans: List[Tuple[int, int]]) -> List[str]:
        distances_from_center = list(map(lambda x: abs(x[1] - len(paragraph) / 2), spans))
        separate_pos = spans[np.argmin(distances_from_center)][1]
        return [paragraph[:separate_pos], paragraph[separate_pos:]]

    # 段落の表示に必要な行数を算出
    def calc_line_num(self, paragraph: str, spans: List[Tuple[int, int]]) -> int:
        line_num = 0
        prev_pos = 0
        for span in spans:
            chara_num = span[1] - prev_pos
            line_num += math.ceil(chara_num / self.max_chara_num_in_line)
            prev_pos = span[1]
        if prev_pos < len(paragraph):
            line_num += 1
        return line_num
