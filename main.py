from charaname_dialogue_separator import CharanameDialogueSeparator
from paragraph_separator import ParagraphSeparator
from line_breaker import LineBreaker


def main():

    max_line_num = 3
    max_chara_num_in_line = 32
    appropriate_max_chara_num_in_line = 28

    charaname_dialogue_separator = CharanameDialogueSeparator()
    paragraph_separator = ParagraphSeparator(max_line_num, max_chara_num_in_line)
    line_breaker = LineBreaker(max_line_num, appropriate_max_chara_num_in_line)

    with open('oinari.txt') as f:
        readed_lines = f.readlines()
        for readed_line in readed_lines:
            readed_line = readed_line.replace('\n', '')
            if len(readed_line) == 0:
                continue
            if readed_line[0] == '#':
                charaname, readed_line = charaname_dialogue_separator.separate(readed_line)
                print(charaname)
            else:
                print('#')
            if readed_line[0] == '　':
                readed_line = readed_line[1:]
            paragraphs = paragraph_separator.separate(readed_line)
            for paragraph in paragraphs:
                breaked_lines = line_breaker.break_line(paragraph)
                for breaked_line in breaked_lines:
                    print(breaked_line)
                print('')


if __name__ == '__main__':
    main()
