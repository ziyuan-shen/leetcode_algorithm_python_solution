# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSymmetricTree(t1, t2):
            if t1==None or t2==None:
                return t1==None and t2==None
            return t1.val == t2.val and isSymmetricTree(t1.left, t2.right) and isSymmetricTree(t1.right, t2.left)
        if root == None:
            return True
        else:
            return isSymmetricTree(root.left, root.right)