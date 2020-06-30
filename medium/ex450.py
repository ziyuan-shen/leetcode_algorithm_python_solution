# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeMin(self, root):
        if not root.left:
            return None, root
        parent = root
        p = root.left
        while p.left:
            parent = parent.left
            p = p.left
        return parent, p
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val == key:
            if root.right:
                parent, p = self.treeMin(root.right)
                if parent:
                    parent.left = p.right
                    p.right = root.right
                p.left = root.left
                return p
            else:
                return root.left
        elif key < root.val:
            left = self.deleteNode(root.left, key)
            root.left = left
        else:
            right = self.deleteNode(root.right, key)
            root.right = right
        return root
                