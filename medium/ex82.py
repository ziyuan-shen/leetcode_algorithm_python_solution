# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prehead = ListNode()
        prehead.next = head
        p1, p2 = prehead, head
        while p2 and p2.next:
            while p2 and p2.next and p2.val != p2.next.val:
                p1 = p2
                p2 = p2.next
            if p2.next:
                value = p2.val
                p2 = p2.next
                while p2 and p2.val == value:
                    p2 = p2.next
                p1.next = p2
        return prehead.next