# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
from collections import deque
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        nodedic = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            node, level = q.popleft()
            nodedic[level].append(node.val)
            if node.left:
                q.append((node.left, level - 1))
            if node.right:
                q.append((node.right, level + 1))
        levels = sorted(nodedic.keys())
        return [nodedic[level] for level in levels]