# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLen(self, head):
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        return length
    
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        length = self.getLen(head)
        if length <= 2:
            return head
        p = head
        for _ in range(length//2):
            p = p.next
        temp = p.next
        p.next = None
        p = temp
        stack = []
        while p:
            stack.append(p)
            p = p.next
        p = head
        while stack:
            temp = p.next
            p.next = stack.pop()
            p = p.next
            p.next = temp
            p = p.next
        return head