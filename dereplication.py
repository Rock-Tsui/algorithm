# coding=utf-8
'''字符串数组去除重复项'''

a = ["aaa", "bbb", "aaa", "ccc", "bbb", "ddadd", "ccc", "aaa", "bbb", "ddd"]
b = list(set(a))  # 用集合的唯一性去重_未排序
>>> ['ddadd', 'aaa', 'bbb', 'ccc', 'ddd']
b.sort(key=a.index)  # 按原始顺序排序
>>> ['aaa', 'bbb', 'ccc', 'ddadd', 'ddd']
# 按字典的keys唯一性去重
c = {}.fromkeys(a).keys()
>>> ['ddadd', 'aaa', 'bbb', 'ccc', 'ddd']
