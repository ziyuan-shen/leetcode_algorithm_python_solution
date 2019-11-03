# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        elif root.left==None and root.right==None:
                return [str(root.val)]
        else:
            left_paths = list(map(lambda x: str(root.val)+'->'+x, self.binaryTreePaths(root.left))) if root.left != None else []
            right_paths = list(map(lambda x: str(root.val)+'->'+x, self.binaryTreePaths(root.right))) if root.right != None else []
            left_paths.extend(right_paths)
            return left_paths