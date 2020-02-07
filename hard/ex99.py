# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        LVR = []
        q = deque([root])
        while True:
            while root.left:
                q.append(root.left)
                root = root.left
            if q:
                node = q.pop()
                LVR.append(node)
                if node.right:
                    q.append(node.right)
                    root = node.right
            else:
                break
        x = y = -1
        for i in range(len(LVR) - 1):
            if LVR[i+1].val < LVR[i].val:
                y = i + 1
                if x == -1:
                    x = i
                else:
                    break
        temp = LVR[x].val
        LVR[x].val = LVR[y].val
        LVR[y].val = temp