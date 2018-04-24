#!/usr/bin/python
# -*- coding:utf8 -*-

from tree.traversal_tree import *

"""
线段树
应用： 区间求和
输入： 数组
返回： 线段树

    线段树特征：
                    根节点
                (start,end)
    左子树                     右子树
(start,(start + end)/2)     ((start+end)/2, end)

"""


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.l = 0
        self.r = 0
        self.val = 0


def create_tree(l, r, arr):
    """
    function: 创建线段树
    :param l: 当前区间的左边界
    :param r: 当前区间的右边界
    :param arr: 数据
    :return: 返回本次调用函数创建的结点
    """

    node = Node()
    node.l = l
    node.r = r
    if l == r:
        node.val = arr[l]
        return node
    m = (l + r) // 2
    node.left = create_tree(l, m, arr)
    node.val += node.left.val
    node.right = create_tree(m + 1, r, arr)
    node.val += node.right.val
    return node


def update_tree(node, i, val):
    """
    function: 更新线段树，将索引为 i 的结点的值更新为 val
    :param node:
    :param i:
    :param val:
    :return:
    """
    # 必须 node.l == node.r，也就是叶子结点，同时 i 和 node.l 相等
    if node.l == node.r and i == node.l:
        node.val = val
        return
    if i <= (node.r + node.l) // 2:
        update_tree(node.left, i, val)
    else:
        update_tree(node.right, i, val)
    node.val = 0
    if node.left:
        node.val = node.left.val
    if node.right:
        node.val += node.right.val
    pass


def sum_range(node, i, j):
    """
    function: 找到 i 到 j 之间的列表元素的和
    :param node:
    :param i:
    :param j:
    :return:
    """
    if i == node.l and j == node.r:
        return node.val
    rs = 0
    m = (node.l + node.r) // 2
    # 这里分为三种情况
    # 1. i <= m < j
    # 2. i < j <= m
    # 3. m <= i< j
    if i <= m and j > m:
        rs += sum_range(node.left, i, m)
        rs += sum_range(node.right, m + 1, j)
    elif i <= m and j <= m:
        rs += sum_range(node.left, i, j)
    else:
        rs += sum_range(node.right, i, j)
    return rs
    pass


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    root = create_tree(0, len(arr) - 1, arr)
    print('层次遍历')
    level_traversal(root)
    print('更新数值')
    update_tree(root, 0, 10)
    level_traversal(root)
    print('求区间值')
    print(sum_range(root, 0, 4))
