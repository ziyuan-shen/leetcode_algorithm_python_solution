# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def insertNode(l, value):
            node = ListNode(value)
            if value<= l.val:
                node.next = l
                return node
            currentList = l
            nextList = l.next
            while nextList != None and value>nextList.val:
                currentList = currentList.next
                nextList = currentList.next
            currentList.next = node
            node.next = nextList
            return l
            
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
            return l1s