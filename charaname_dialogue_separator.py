import re
from typing import Tuple


class CharanameDialogueSeparator:
    def __init__(self):
        pass

    def separate(self, paragraph: str) -> Tuple[str, str]:

        if len(paragraph) == 0 or paragraph[0] != '#':
            return None, None

        spans = [match.span() for match in re.finditer('[「『]', paragraph)]
        if len(spans) == 0:
            return None, None

        return paragraph[:spans[0][0]], paragraph[spans[0][0]:]


def main():
    charaname_dialogue_separator = CharanameDialogueSeparator()
    charaname, dialogue = charaname_dialogue_separator.separate('#タマ「こんにちは」')
    print('hoge')


if __name__ == '__main__':
    main()
