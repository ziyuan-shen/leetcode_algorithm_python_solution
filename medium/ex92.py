# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prehead = ListNode(-1)
        prehead.next = head
        idx = 1
        p = prehead
        while idx < m:
            p = p.next
            idx += 1
        stack = []
        p2 = p.next
        while idx <= n:
            stack.append(p2)
            idx += 1
            p2 = p2.next
        while stack:
            node = stack.pop()
            p.next = node
            p = p.next
        p.next = p2
        return prehead.next