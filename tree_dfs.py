# from ast import List


from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# https://blog.csdn.net/oyall520/article/details/104828561
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []  # 用来保存一路遇到的节点未遍历的右分支
        res = []  # 用来存储前序遍历的节点的值
        node = root
        while stack or node: # 当栈不为空或者节点不为空时说明还需要遍历，进入循环
            while node: # 当前节点不为空时，就沿着左分支下行
                res.append(node.val) # 先将当前节点的值添加到res储存起来（即处理根节点数据）
                stack.append(node.right) # 将当前节点的右分支入栈
                node = node.left  # 沿着左分支下行
            node = stack.pop() # 遇到空树，回溯
        return res

# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res=[]
#         stack=[]
#         node=root
#         while stack or node:
            


tree=TreeNode(0)
tree.left=TreeNode(1)
tree.right=TreeNode(2)
tree.left.left=TreeNode(3)
tree.left.right=TreeNode(4)

solution=Solution()
res=solution.preorderTraversal(tree)
print("res")
print(res)
# res
# [0, 1, 3, 4, 2]