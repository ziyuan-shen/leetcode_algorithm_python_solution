# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSumFromRoot(self, root, sum):
        if not root:
            return 0
        ans = 0
        if root.val == sum:
            ans += 1
        ans += self.pathSumFromRoot(root.left, sum - root.val)
        ans += self.pathSumFromRoot(root.right, sum - root.val)
        return ans
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        ans = 0
        if root.val == sum:
            ans += 1
        ans += self.pathSum(root.left, sum)
        ans += self.pathSumFromRoot(root.left, sum - root.val)
        ans += self.pathSum(root.right, sum)
        ans += self.pathSumFromRoot(root.right, sum - root.val)
        return ans