# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        prehead = ListNode(-1)
        prehead.next = head
        prev = prehead
        while prev:
            stack = []
            p = prev.next
            while p and len(stack) < k:
                stack.append(p)
                p = p.next
            if len(stack) == k:
                while stack:
                    prev.next = stack.pop()
                    prev = prev.next
                prev.next = p
            else:
                break
        return prehead.next