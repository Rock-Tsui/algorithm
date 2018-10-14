# coding=utf-8


def get_LCSubSeq(s1, s2):
    '''求最长公共子序列'''
    l1 = len(s1)
    l2 = len(s2)
    maxLen = [[0] * (l2 + 2) for _ in range(l1 + 2)]

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                maxLen[i][j] = maxLen[i - 1][j - 1] + 1
            else:
                maxLen[i][j] = max(maxLen[i][j - 1], maxLen[i - 1][j])

    return maxLen[l1][l2]


def get_LCSubStr(s1, s2):
    '''求最长公共子串'''
    l1 = len(s1)
    l2 = len(s2)
    maxLen = [[0] * (l2 + 2) for _ in range(l1 + 2)]

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                maxLen[i][j] = maxLen[i - 1][j - 1] + 1

    return maxLen[l1][l2]


if __name__ == '__main__':
    print(get_LCSubSeq('abcdfg','abdfg'))
    print(get_LCSubStr('abcdfg','abdfg'))
