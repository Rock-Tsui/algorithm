#coding=utf-8
'''在一个已经排序的Int数组中，查找某个number，
如果存在这个number，返回在数组的位置，反之返回-1'''
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_index(data, sIndex, eIndex):
    global L
    mid_index = (eIndex - sIndex) // 2 + sIndex
    
    if L[sIndex] > data or L[eIndex] < data:
        return -1
    if L[mid_index] > data:
        return get_index(data, sIndex, mid_index)
    elif L[mid_index] < data:
        return get_index(data, mid_index + 1, eIndex)
    else:
        return mid_index


if __name__ == '__main__':
    index = get_index(9, 0, 8)
    print(index)
