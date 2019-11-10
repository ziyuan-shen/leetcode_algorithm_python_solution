# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def insertNode(self, head, val):
        if head == None:
            return ListNode(val)
        else:
            prehead = ListNode(-1)
            prehead.next = head
            pointer1 = prehead
            pointer2 = head
            while pointer2 != None and pointer2.val<val:
                pointer1 = pointer1.next
                pointer2 = pointer2.next
            node = ListNode(val)
            node.next = pointer2
            pointer1.next = node
            return prehead.next
        
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        head = lists[0]
        for linked_list in lists[1:]:
            pointer = linked_list
            while pointer!=None:
                head = self.insertNode(head, pointer.val)
                pointer = pointer.next
        return head