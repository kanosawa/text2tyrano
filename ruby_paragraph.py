from ruby_morpheme import RubyMorpheme


class RubyParagraph:
    def __init__(self):
        self.ruby_morpheme = RubyMorpheme()

    def ruby(self, paragraph: str) -> str:

        self.ruby_morpheme.ruby()


def main():
    ruby_paragraph = RubyParagraph()
    ruby_paragraph.ruby()


if __name__ == '__main__':
    main()
