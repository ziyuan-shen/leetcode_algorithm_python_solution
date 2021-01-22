# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def placeCamera(self, root, monitored):
        if not root:
            return 0
        if (root, monitored) in self.mem:
            return self.mem[(root, monitored)]
        if monitored:
            self.mem[(root, monitored)] = min(self.placeCamera(root.left, False) + self.placeCamera(root.right, False), 1 + self.placeCamera(root.left, True) + self.placeCamera(root.right, True))
            return self.mem[(root, monitored)]
        else:
            ans = 1 + self.placeCamera(root.left, True) + self.placeCamera(root.right, True)
            if root.left:
                ans = min(ans, 1 + self.placeCamera(root.left.left, True) + self.placeCamera(root.left.right, True) + self.placeCamera(root.right, False))
            if root.right:
                ans = min(ans, 1 + self.placeCamera(root.right.left, True) + self.placeCamera(root.right.right, True) + self.placeCamera(root.left, False))
            if root.left and root.right:
                ans = min(ans, 2 + self.placeCamera(root.left.left, True) + self.placeCamera(root.left.right, True) + self.placeCamera(root.right.left, True) + self.placeCamera(root.right.right, True))
            self.mem[(root, monitored)] = ans
            return ans
        
    def minCameraCover(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.mem = {}
        return self.placeCamera(root, False)