import re
from typing import Tuple


# キャラ名とセリフを分割するクラス
#
# '#'とカギカッコで判別
class CharanameDialogueSeparator:
    def __init__(self):
        pass

    # 分割する
    def separate(self, paragraph: str) -> Tuple[str, str]:

        if len(paragraph) == 0 or paragraph[0] != '#':
            return None, None

        spans = [match.span() for match in re.finditer('[「『]', paragraph)]
        if len(spans) == 0:
            return None, None

        return paragraph[:spans[0][0]], paragraph[spans[0][0]:]
