# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        prehead1 = ListNode()
        prehead2 = ListNode()
        p1 = prehead1
        p2 = prehead2
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        p2.next = None
        p1.next = prehead2.next
        return prehead1.next