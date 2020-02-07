# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
from collections import deque
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        vlinedic = defaultdict(list)
        q = deque([(0, 0, root)])
        while q:
            x, y, node = q.popleft()
            vlinedic[x].append((y, node.val))
            if node.left:
                q.append((x - 1, y + 1, node.left))
            if node.right:
                q.append((x + 1, y + 1, node.right))
        ans = []
        for x in sorted(list(vlinedic.keys())):
            vals = vlinedic[x]
            vals.sort()
            ans.append([val[1] for val in vals])
        return ans