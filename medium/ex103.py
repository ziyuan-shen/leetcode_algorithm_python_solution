# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root, 0)])
        ans = [[]]
        current_level = 0
        while q:
            node, level = q.popleft()
            if level == current_level:
                if level % 2 == 1:
                    ans[-1].insert(0, node.val)
                else:
                    ans[-1].append(node.val)
            else:
                current_level = level
                ans.append([node.val])
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return ans