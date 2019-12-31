# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def copyTree(self, root):
        if root == None:
            return None
        new = TreeNode(root.val)
        new.left = self.copyTree(root.left)
        new.right = self.copyTree(root.right)
        return new
    
    def maxPathSum(self, root):
        root_copy = self.copyTree(root)
        def nodeLRV(root):
            if root != None:
                nodeLRV(root.left)
                nodeLRV(root.right)
                if root.right == None and root.left == None:
                    return None
                elif root.right == None:
                    root.val += max(root.left.val, 0)
                elif root.left == None:
                    root.val += max(root.right.val, 0)
                else:
                    root.val += max(root.left.val, root.right.val, 0)
        nodeLRV(root_copy)
        def pathLRV(root, node_root):
            if root != None:
                pathLRV(root.left, node_root.left)
                pathLRV(root.right, node_root.right)
                if root.right == None and root.left == None:
                    return None
                elif root.right == None:
                    root.val = max(root.left.val, node_root.val)
                elif root.left == None:
                    root.val = max(root.right.val, node_root.val)
                else:
                    left = node_root.left.val
                    right = node_root.right.val
                    root.val = max(left+right+root.val, left+root.val, right+root.val, root.val, root.left.val, root.right.val)
        pathLRV(root, root_copy)
        return root.val