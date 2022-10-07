import pykakasi
import regex


# 漢字のグレード（習う学年）を算出するクラス
#
# 小学校で習う漢字は1～6、中学校以降で習う漢字は7、常用外漢字は8を返す
# 複数の漢字を含む文字列が入力された場合は、最大グレードを返す
class KanjiGradeCalculator:
    def __init__(self, joyo_path: str):
        self.kks = pykakasi.kakasi()
        self.kanji2grade = dict()
        with open(joyo_path, encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[1:]:
                kanji = line[0]
                grade = line[3:].split()[1].replace('S', '')
                self.kanji2grade[kanji] = grade

    def calculate(self, str_in: str) -> int:
        converted_list = self.kks.convert(str_in)
        max_grade = 0
        for converted in converted_list:
            morpheme = converted['orig']
            for moji in morpheme:
                if regex.match('^\p{Script=Han}+$', moji) is not None:
                    max_grade = max(max_grade, self.get_grade(moji))
        return max_grade

    def get_grade(self, moji: str) -> int:
        grade = self.kanji2grade.get(moji)
        return 8 if grade is None else int(grade)


def main():
    calculator = KanjiGradeCalculator('joyo2010.txt')
    str_in = '躁鬱'
    grade = calculator.calculate(str_in)
    print(grade)


if __name__ == '__main__':
    main()
