# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        VLR = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                VLR.append(None)
            else:
                VLR.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return "#".join([str(x) for x in VLR])
    
    def create_tree(self, VLR):
        val = VLR.pop(0)
        if val == None:
            return None
        else:
            node = TreeNode(val)
            node.left = self.create_tree(VLR)
            node.right = self.create_tree(VLR)
            return node

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        VLR = data.split("#")
        VLR = [None if x == "None" else int(x) for x in VLR]
        return self.create_tree(VLR)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))