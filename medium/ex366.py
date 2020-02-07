# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isLeaf(self, root):
        return not (root.left or root.right)
        
    def collectLeaves(self, root):
        if root.left:
            if self.isLeaf(root.left):
                self.leaves[-1].append(root.left.val)
                root.left = None
            else:
                self.collectLeaves(root.left)
        if root.right:
            if self.isLeaf(root.right):
                self.leaves[-1].append(root.right.val)
                root.right = None
            else:
                self.collectLeaves(root.right)
        
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.leaves = []
        while not self.isLeaf(root):
            self.leaves.append([])
            self.collectLeaves(root)
        self.leaves.append([root.val])
        return self.leaves