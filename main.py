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

    with open('Event01.ks', 'w', encoding='utf-8', newline='\n') as fw:
        fw.write('[tb_start_text mode=4]\n')
        with open('Event01.txt', encoding='utf-8') as fr:
            readed_lines = fr.readlines()
            last_bracket_flag = False
            first_flag = True
            for readed_line in readed_lines:
                readed_line = readed_line.replace('\n', '')

                # 改行のみの行を飛ばす
                if len(readed_line) == 0:
                    continue

                # 発言者
                if readed_line[0] == '#':
                    if not first_flag:
                        fw.write('[_tb_end_text]\n\n[tb_start_text mode=4]\n')
                    charaname, readed_line = charaname_dialogue_separator.separate(readed_line)
                    fw.write(charaname + '\n')
                # 台詞の次の行で、かつ台詞じゃない場合は地の文の開始
                elif last_bracket_flag:
                    fw.write('[_tb_end_text]\n\n[tb_start_text mode=4]\n#\n')
                last_bracket_flag = False

                if first_flag:
                    first_flag = False

                if readed_line[0] == '　':
                    readed_line = readed_line[1:]

                paragraphs = paragraph_separator.separate(readed_line)
                for paragraph in paragraphs:
                    breaked_lines = line_breaker.break_line(paragraph)
                    for i, breaked_line in enumerate(breaked_lines):
                        break_symbol = '[p]\n' if i == len(breaked_lines) - 1 else '[r]\n'
                        fw.write(breaked_line + break_symbol)
                    if breaked_line[-1] == '」':
                        last_bracket_flag = True

        fw.write('[_tb_end_text]\n')


if __name__ == '__main__':
    main()
