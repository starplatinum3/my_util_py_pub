# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from numpy import rot90
from TreeNode import TreeNode


class Solution:
    def pre(self,root,node):
        if root==None:
            return
        # root.val
        # node.right
        nn=TreeNode(root.val)
        node.right=nn
        # node=TreeNode()
        self.pre(root.left, node.right)
        self.pre(root.right, node.right)
        


    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        newRoot=TreeNode(root.val)
        self.pre(root,newRoot)
        # newRoot=root
        root=newRoot