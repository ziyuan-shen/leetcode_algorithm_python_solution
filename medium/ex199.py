# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        q = deque([])
        if root:
            q.append((root, 1))
        ans = []
        next_level = 1
        while q:
            node, level = q.popleft()
            if level == next_level:
                ans.append(node.val)
                next_level += 1
            if node.right:
                q.append((node.right, level + 1))
            if node.left:
                q.append((node.left, level + 1))
        return ans