# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prehead = ListNode(-1)
        prehead.next = head
        kept_head = prehead
        current_node = head
        while current_node != None:
            if current_node.val == val:
                next_node = current_node.next
                prehead.next = next_node
                current_node = next_node
                continue
            prehead = prehead.next
            current_node = current_node.next
        return kept_head.next