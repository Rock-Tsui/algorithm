#!/usr/bin/env python
# coding=utf-8
'''
    7
   3 8
  8 1 0
 2 7 4 4
4 5 2 6 5
在上面的数字三角形中寻找一条从顶部到底边的路径，
使得路径上所经过的数字之和最大。路径上的每一步都只
能往左下或右下走。只需要求出这个最大和即可，不必给
出具体路径。三角形的行数大于1小于等于100，数字为0-99'''
import random

MAX = 10
subSet = [[-1] * MAX for _ in range(MAX)]


def getMaxSum(n):
    global subSet

    maxSum = subSet[n]
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            maxSum[j] = max(maxSum[j], maxSum[j + 1]) + subSet[i][j]
    return maxSum[1]


if __name__ == '__main__':
    # n = int(input('input n: '))
    n = 5
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            subSet[i][j] = random.randint(0, 9)
    print(getMaxSum(n))
