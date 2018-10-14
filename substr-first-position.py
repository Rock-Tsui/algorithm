# coding=utf-8
'''在字符串中找到子字符串第一次出现的位置.
从str1中截取和str2长度一样的字符串，
和str2比较，相等即找到，不相等再截取一个新的字符串。
直到找到或找不到。'''


def str_first_position(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    start = 0
    while start <= len1 - len2:
        if str1[start:start + len2] == str2:
            return start
        start += 1
    return None


if __name__ == '__main__':
    pos = str_first_position('abcdefghijklmn', 'cde')
    print(pos)
