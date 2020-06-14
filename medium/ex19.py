# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        count = 0
        while p:
            count += 1
            p = p.next
        prev = ListNode
        prev.next = head
        p = prev
        for _ in range(count - n):
            p = p.next
        temp = p.next.next
        p.next = temp
        return prev.next