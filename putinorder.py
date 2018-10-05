# coding=utf-8
'''将一个未排序的整形数组进行归置，数组中的负数移动到数组的左边，
正数移动到数组的右边。0不动(ps:我一开做这题就打算用无脑排序搞定，
结果我才开始写，面试官就说了"这里需要提示一下，移动后的数组只是负数在左，
正数在右。不一定非要用传统的排序，如果不是传统的排序可以加分'''

L = [8, -5, 4, 0, -9]


def putinorder():
    global L
    left = 0
    right = len(L) - 1
    while left != right:
        while L[right] > 0:
            right -= 1
        while L[left] < 0:
            left += 1

        temp = L[right]
        L[right] = L[left]
        L[left] = temp
    print(L)
if __name__ == '__main__':
    putinorder()

