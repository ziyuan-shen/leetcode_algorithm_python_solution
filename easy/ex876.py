# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        mid = length // 2 + 1
        p = head
        count = 1
        while count < mid:
            count += 1
            p = p.next
        return p