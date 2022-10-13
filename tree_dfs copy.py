# from ast import List


from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        stack=[]
        node=root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node.right)
                node=node.left
            stack.pop(node)
        return res
                


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