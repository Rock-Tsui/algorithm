# coding=utf-8
'''{"12,bob","3,sky","6,cool","1,good","22,go"}，
按元素第一列排序'''
L = {"12,bob","3,sky","6,cool","1,good","22,go"}


def sortbynum():
    global L
    D ={}
    l = list(L)
    ret = map(lambda x:{int(x.split(',')[0]):x}, l)
    for i in ret:
        D.update(i)
    for key in sorted(D.keys()):
        yield D[key]


if __name__ == '__main__':
    l = sortbynum()
    print(list(l))
