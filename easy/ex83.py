# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p and p.next:
            if p.val == p.next.val:
                temp = p.next.next
                p.next = temp
            else:
                p = p.next
        return head