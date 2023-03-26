import regex
import pykakasi


def main():

    kanji_grade_dict = dict()
    with open('joyo2010.txt', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            kanji = line[0]
            grade = line[3:].split()[1].replace('S', '')
            kanji_grade_dict[kanji] = grade

    kks = pykakasi.kakasi()
    paragraph = '霧ヶ峰'
    results = kks.convert(paragraph)

    for result in results:
        morpheme = result['orig']
        hira_idx = 0
        for moji_idx, moji in enumerate(morpheme):
            if regex.match('^\p{Script=Han}+$', moji) is not None:
                grade = kanji_grade_dict.get(moji)
                if grade is None or int(grade) == 7:
                    print('ふりがな')
            else:
                hira_idx += 1


if __name__ == '__main__':
    main()
