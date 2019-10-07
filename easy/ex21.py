# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def insertNode(l, value):
            node = ListNode(value)
            prehead = ListNode(-1)
            prehead.next = l
            reserve = prehead
            while prehead.next != None and value>prehead.next.val:
                prehead = prehead.next
            node.next = prehead.next
            prehead.next = node
            return reserve.next
            
        if l1==None and l2==None:
            return None
        elif l1==None:
            return l2
        elif l2==None:
            return l1
        else:
            currentList = l2
            while currentList != None:
                l1 = insertNode(l1, currentList.val)
                currentList = currentList.next
            return l1