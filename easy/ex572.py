# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isEqual(t1, t2):
            if t1==None or t2==None:
                return t1==None and t2==None
            else:
                return t1.val == t2.val and isEqual(t1.left, t2.left) and isEqual(t1.right, t2.right)
        if s==None:
            return t==None
        if isEqual(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)