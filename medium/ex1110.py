# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delete(self, root, to_delete):
        if not root:
            return False, []
        for idx in range(len(to_delete)):
            if root.val == to_delete[idx]:
                del to_delete[idx]
                return False, self.delete(root.left, to_delete)[1] + self.delete(root.right, to_delete)[1]
        left_root, left_forest = self.delete(root.left, to_delete)
        right_root, right_forest = self.delete(root.right, to_delete)
        if left_root:
            root.left = left_forest.pop(0)
        else:
            root.left = None
        if right_root:
            root.right = right_forest.pop(0)
        else:
            root.right = None
        return True, [root] + left_forest + right_forest
        
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        return self.delete(root, to_delete)[1]
                