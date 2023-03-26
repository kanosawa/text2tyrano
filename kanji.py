import regex


def main():
    str = 'あ'
    res = regex.match('^\p{Script=Han}+$', str)
    print('hoge')


if __name__ == '__main__':
    main()
