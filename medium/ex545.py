# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        VLR = deque([])
        q = deque([(root, "root")])
        while q:
            node, position = q.pop()
            VLR.append((node, position))
            if node.right:
                if position == 'root' or position == "right_boundary":
                    q.append((node.right, "right_boundary"))
                elif position == "left_boundary" and not node.left:
                    q.append((node.right, "left_boundary"))
                else:
                    q.append((node.right, "middle"))
            if node.left:
                if position == "root" or position == "left_boundary":
                    q.append((node.left, "left_boundary"))
                elif position == "right_boundary" and not node.right:
                    q.append((node.left, "right_boundary"))
                else:
                    q.append((node.left, "middle"))
        ans = [VLR[0][0].val]
        VLR.popleft()
        right = []
        for node, position in VLR:
            if position == "left_boundary" or (not node.left and not node.right):
                ans.append(node.val)
            elif position == "right_boundary":
                right.append(node.val)
        return ans + right[::-1]