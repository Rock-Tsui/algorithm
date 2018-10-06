#coding=utf-8
'''Binary Tree Traversal'''


class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def PreOderTraverse(biTree):
    '''前序遍历'''
    if not biTree:
        return
    print(biTree.value)
    PreOderTraverse(biTree.left)
    PreOderTraverse(biTree.right)


def MidOderTraverse(biTree):
    '''中序遍历'''
    if not biTree:
        return
    MidOderTraverse(biTree.left)
    print(biTree.value)
    MidOderTraverse(biTree.right)


def LastOderTraverse(biTree):
    '''后序遍历'''
    if not biTree:
        return
    LastOderTraverse(biTree.left)
    LastOderTraverse(biTree.right)
    print(biTree.value)


'''
如果我们已知二叉树的前序遍历和中序遍历，求这棵二叉树的后序遍历
preList = list('12473568')
midList = list('47215386')
afterList = []

def findTree(preList, midList, afterList):
    if len(preList) == 0:
        return
    if len(preList) == 1:
        afterList.append(preList[0])
        return
    root = preList[0]
    n = midList.index(root)
    findTree(preList[1:n + 1], midList[:n], afterList)
    findTree(preList[n + 1:], midList[n + 1:], afterList)
    afterList.append(root)
'''

if __name__ == '__main__':
    biTree = Node('D',
                  Node('B', Node('A'), Node('C')),
                  Node('E', right=Node('G', Node('F'))))
    PreOderTraverse(biTree)
    print('=' * 10)
    MidOderTraverse(biTree)
    print('=' * 10)
    LastOderTraverse(biTree)
