# coding: utf-8

import pinyin

def main():
    string = '熊猫科技'
    print pinyin.get(string)
    print pinyin.get(string, format="strip")
    print pinyin.get(string, format="strip", delimiter=" ")
    print pinyin.get_initial(string)

if __name__ == '__main__':
    main()