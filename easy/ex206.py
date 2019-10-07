# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prehead = ListNode(-1)
        curnode = head
        while curnode!= None:
            node = ListNode(curnode.val)
            node.next = prehead.next
            prehead.next = node
            curnode = curnode.next
        return prehead.next