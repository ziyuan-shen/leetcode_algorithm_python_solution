# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
from collections import deque
class Solution:
    def VLR(self, node, neighbordic):
        if node.left:
            neighbordic[node.val].add(node.left.val)
            neighbordic[node.left.val].add(node.val)
            self.VLR(node.left, neighbordic)
        if node.right:
            neighbordic[node.val].add(node.right.val)
            neighbordic[node.right.val].add(node.val)
            self.VLR(node.right, neighbordic)
        
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if K == 0:
            return [target.val]
        neighbordic = defaultdict(set)
        self.VLR(root, neighbordic)
        start = target.val
        q = deque([(start, 0)])
        visited = {node: False for node in neighbordic}
        visited[start] = True
        ans = []
        while q:
            node, level = q.popleft()
            for neighbor in neighbordic[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    if level == K-1:
                        ans.append(neighbor)
                    q.append((neighbor, level+1))
        return ans