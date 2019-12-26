# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def getDepth(self, root):
        if root == None:
            return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))
    
    def recursiveSerialize(self, root, depth):
        if depth == 0:
            return []
        if depth == 1:
            if root == None:
                return [None]
            else:
                return [root.val]
        if root == None:
            return [None] + self.recursiveSerialize(None, depth - 1) * 2
        return [root.val] + self.recursiveSerialize(root.left, depth - 1) + self.recursiveSerialize(root.right, depth - 1)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        depth = self.getDepth(root)
        return str(self.recursiveSerialize(root, depth))[1:-1]
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        data = data.split(', ')
        if data[0] == 'None':
            return None
        root = TreeNode(int(data[0]))
        depth = int((len(data) - 1) / 2)
        root.left = self.deserialize(', '.join(data[1:1+depth]))
        root.right = self.deserialize(', '.join(data[1+depth:]))
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))