# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

# from LeetCode.TreeNode import TreeNode
from TreeNode import TreeNode

class Solution:
    def pre(self,root:TreeNode,lst:List[int]):
        # print(root.val)
        if root==None:
            return
        lst.append(root.val)
        # print(root.val)
        self.pre(root.left,lst)
        self.pre(root.right,lst)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst=[]
        self.pre(root,lst)
        print("lst")
        print(lst)
        return lst
