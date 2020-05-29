# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_sort(self, head):
        if head.next:
            length = 0
            p = head
            while p != None:
                length += 1
                p = p.next
            mid = head
            for i in range(length//2-1):
                mid = mid.next
            head2 = mid.next
            mid.next = None
            head1 = self.merge_sort(head)
            head2 = self.merge_sort(head2)
            head = self.merge(head1, head2)
        return head
        
    def merge(self, head1, head2):
        prehead = ListNode()
        p = prehead
        p1 = head1
        p2 = head2
        while p1 or p2:
            if p1 and p2:
                if p1.val < p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
            elif p1:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
            p.next = None
        return prehead.next
        
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        return self.merge_sort(head)
        
        