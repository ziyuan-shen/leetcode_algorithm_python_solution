# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getNodeNum(self, root):
        if root in self.nodeNumDict:
            return self.nodeNumDict[root]
        else:
            if not root:
                return 0
            ans = 1 + self.getNodeNum(root.left) + self.getNodeNum(root.right)
            self.nodeNumDict[root] = ans
            return ans
    
    def getValSum(self, root):
        if root in self.valSumDict:
            return self.valSumDict[root]
        else:
            if not root:
                return 0
            ans = root.val +self.getValSum(root.left) + self.getValSum(root.right)
            self.valSumDict[root] = ans
            return ans
        
    def dfs(self, root):
        self.move += abs(self.getNodeNum(root) - self.getValSum(root))
        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)
            
    def distributeCoins(self, root: TreeNode) -> int:
        self.move = 0
        self.nodeNumDict = dict()
        self.valSumDict = dict()
        self.dfs(root)
        return self.move