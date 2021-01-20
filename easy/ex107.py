# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        q = deque([(1, root)])
        current_level = 1
        ans = [[]]
        while q:
            level, node = q.popleft()
            if level == current_level:
                ans[0].append(node.val)
            else:
                ans.insert(0, [node.val])
                current_level = level
            if node.left:
                q.append((level + 1, node.left))
            if node.right:
                q.append((level + 1, node.right))
        return ans