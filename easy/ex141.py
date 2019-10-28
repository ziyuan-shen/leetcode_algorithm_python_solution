# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        slow_pointer = head
        fast_pointer = head.next
        while True:
            if slow_pointer == fast_pointer:
                return True
            if slow_pointer.next == None or fast_pointer.next==None or fast_pointer.next.next == None:
                return False
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next