# 使用 7 种方式遍历二叉树
# 递归：前序，中序，后序
# 非递归：前序，中序，后序，层次
# 首先定义一棵树

class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

# 构造一棵树
def construct_tree(treelist,i):
    if i <len(treelist) and tree_list[i] != None:
        node = Tree(treelist[i])
    else:
        return
    if 2*i+1<len(treelist):
        node.left = construct_tree(treelist,2*i+1)
    if 2*i+2<len(treelist):
        node.right = construct_tree(treelist,2*i+2)
    return node

# 先序遍历
def pre(node):
    if node:
        print(node.val)
    if node.left:
        pre(node.left)
    if node.right:
        pre(node.right)

# 中序遍历
def mid(node):
    if node:
        if node.left:
            mid(node.left)
        print(node.val)
        if node.right:
            mid(node.right)

# 后序遍历
def last(node):
    if node:
        if node.left:
            last(node.left)
        if node.right:
            last(node.right)
        print(node.val)

# 无递归先序遍历
def pre_no_recursion(node):
    pass

# 无递归中序遍历
def mid_no_recursion(node):
    pass

# 无递归后序遍历
def last_no_recursion(node):
    pass

# 层次遍历
def level_traversal(node):
    pass

tree_list = [1,5,2]
node = construct_tree(tree_list,0)
print('先序遍历：')
pre(node)
print('中序遍历')
mid(node)
print('后序遍历')
last(node)
