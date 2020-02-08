# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p1 = head
        even_head = head.next
        p2 = even_head
        while p2 and p2.next:
            p1.next = p2.next
            p1 = p2.next
            p2.next = p1.next
            p2 = p1.next
        p1.next = even_head
        return head