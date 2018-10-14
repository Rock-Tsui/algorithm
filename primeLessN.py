#!/usr/bin/env python
# coding=utf-8
'''求小于n的最大素数'''
import math


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def primeLessN(N):
    for i in range(N, 1, -1):
        if isPrime(i):
            return i


if __name__ == '__main__':
    print(primeLessN(100000))
