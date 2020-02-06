# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        valdic = defaultdict(list)
        q = deque([(0, root)])
        while q:
            level, node = q.popleft()
            valdic[level].append(node.val)
            if node.left:
                q.append((level + 1, node.left))
            if node.right:
                q.append((level + 1, node.right))
        ans = []
        for i in range(len(valdic)):
            ans.append(valdic[i])
        return ans