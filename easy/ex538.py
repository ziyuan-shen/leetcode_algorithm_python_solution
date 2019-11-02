# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def sumBST(root):
            if root==None:
                return 0
            return root.val + sumBST(root.left) + sumBST(root.right)
        
        def addConstant(root, constant):
            if root == None:
                return None
            root.val += constant
            root.left = addConstant(root.left, constant)
            root.right = addConstant(root.right, constant)
            return root
            
        if root == None:
            return None
        root.left = addConstant(self.convertBST(root.left), root.val+sumBST(root.right))
        root.val += sumBST(root.right)
        root.right = self.convertBST(root.right)
        return root
        