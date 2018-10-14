#coding=utf-8
'''在一个已经排序的Int数组中，查找某个number，
如果存在这个number，返回True，反之返回False'''


def binary_chop(alist, data):
    '''递归解决二分查找'''
    n = len(alist)
    mid = n//2

    if n < 1:
        return False
    if alist[mid] > data:
        return binary_chop(alist[:mid], data)
    elif alist[mid] < data:
        return binary_chop(alist[mid+1:], data)
    else:
        return True

def binary_chop1(alist, data):
    '''非递归解决二分查找'''
    n = len(alist)
    first = 0
    last = n - 1

    while first <= last:
        mid = (last + first) // 2
        if alist[mid] > data:
            last = mid - 1
        elif alist[mid] <data:
            first = mid + 1
        else:
            return True
    return False



if __name__ == '__main__':
    alist = [2,4,5,12,14,23]
    print(binary_chop1(alist, 23))
