# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prehead = ListNode(-1)
        prehead.next = head
        prev = prehead
        p = head
        while p and p.next:
            nextpair = p.next.next
            prev.next = p.next
            p.next.next = p
            p.next = nextpair
            prev = p
            p = p.next
        return prehead.next