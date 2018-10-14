#coding=utf-8
'''在一个已经排序的Int数组中，查找某个number，
如果存在这个number，返回在数组的位置，反之返回-1'''
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_index(data, sIndex, eIndex):
    '''递归'''
    global L
    midIndex = (eIndex + sIndex) // 2

    if L[sIndex] > data or L[eIndex] < data:
         return -1
    if L[midIndex] > data:
        return get_index(data, sIndex, midIndex)
    elif L[midIndex] < data:
        return get_index(data, midIndex + 1, eIndex)
    else:
        return midIndex

def get_index1(alist, data):
    '''非递归'''
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
            return mid
    return -1

if __name__ == '__main__':
    #print(get_index(9, 0, 8))
    print(get_index1(L, 1))
