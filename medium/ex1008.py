# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from bisect import bisect
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        idx = bisect(preorder[1:], preorder[0])
        return TreeNode(preorder[0], self.bstFromPreorder(preorder[1:][:idx]), self.bstFromPreorder(preorder[1:][idx:]))