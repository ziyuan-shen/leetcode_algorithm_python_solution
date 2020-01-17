# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.data = self.serialize(root)
        self.count = 0
        
    def serialize(self, root):
        if not root:
            return []
        return self.serialize(root.left) + [root.val] + self.serialize(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.count += 1
        return self.data[self.count-1]
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.count < len(self.data)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()