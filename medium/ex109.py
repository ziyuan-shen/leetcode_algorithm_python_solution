# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: 
    def generateBST(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        idx = len(nums) // 2
        root = TreeNode(nums[idx])
        root.left = self.generateBST(nums[:idx])
        root.right = self.generateBST(nums[idx + 1:])
        return root
        
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        nums = []
        p = head
        while p:
            nums.append(p.val)
            p = p.next
        return self.generateBST(nums)