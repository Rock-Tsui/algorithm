L = [5, 1, 11, 7, 13, 4, 8, 3, 9, 6]


def QSorted(_left, _right):
    global L
    left, right = _left, _right
    if left >= right:
        return
    base = L[left]

    while left != right:
        while L[right] >= base and right > left:
            right -= 1

        while L[left] <= base and right > left:
            left += 1

        temp = L[left]
        L[left] = L[right]
        L[right] = temp

    L[_left] = L[left]
    L[left] = base

    QSorted(_left, left - 1)
    QSorted(right + 1, _right)


if __name__ == '__main__':
    QSorted(0, 9)
    print(L)
