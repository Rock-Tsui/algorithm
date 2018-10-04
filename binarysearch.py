#coding=utf-8
'''在一个已经排序的Int数组中，查找某个number，
如果存在这个number，返回在数组的位置，反之返回-1'''
L = [8, 7, 6, 5, 4, 3, 2, 1]


def get_index(num, start, end):
    global L
    if num > L[start] or num < L[end]:
        return -1
    if num == L[end]:
        return end
    if num == L[start]:
        return start
    if num > L[(end - start + 1) // 2 + start]:
        return get_index(num, start, ((end - start + 1) // 2 + start) - 1)
    elif num < L[(end - start + 1) // 2 + start]:
        return get_index(num, (end - start + 1) // 2 + start, end)
    elif num == L[(end - start + 1) // 2 + start]:
        return (end - start + 1) // 2 + start


if __name__ == '__main__':
    index = get_index(6, 0, 7)
    print(index)
