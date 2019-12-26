# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:   
    def recursiveSerialize(self, root):
        if root == None:
            return [None]
        else:
            return [root.val] + self.recursiveSerialize(root.left) + self.recursiveSerialize(root.right)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return str(self.recursiveSerialize(root))[1:-1]
    
    def recursiveDeserialize(self, data):
        if data[0] == 'None':
            data.pop(0)
            return None
        else:
            root = TreeNode(int(data[0]))
            data.pop(0)
            root.left = self.recursiveDeserialize(data)
            root.right = self.recursiveDeserialize(data)
            return root
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(', ')
        return self.recursiveDeserialize(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))