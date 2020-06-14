# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            root = stack.pop()
            ans.append(root.val)
            root = root.right
            while root:
                stack.append(root)
                root = root.left
        return ans