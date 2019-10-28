# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        current_node = head
        l = []
        while current_node != None:
            l.append(current_node)
            current_node = current_node.next
            if current_node in l:
                return True