# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        p = head
        length = 0
        while p:
            length += 1
            p = p.next
        move = length - k % length
        if move == length:
            return head
        p = head
        for _ in range(move - 1):
            p = p.next
        ans = p.next
        p.next = None
        p = ans
        while p.next:
            p = p.next
        p.next = head
        return ans