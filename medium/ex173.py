# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []
        if root:
            self.stack.append(root)
            node = root
            while node.left:
                self.stack.append(node.left)
                node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        top = self.stack.pop()
        if top.right:
            self.stack.append(top.right)
            node = top.right
            while node.left:
                self.stack.append(node.left)
                node = node.left
        return top.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()