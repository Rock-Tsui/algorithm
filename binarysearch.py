#coding=utf-8
'''在一个已经排序的Int数组中，查找某个number，
如果存在这个number，返回在数组的位置，反之返回-1'''


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

if __name__ == '__main__':
    alist = [2,4,5,12,14,23]
    index = binary_chop(alist, 23)
