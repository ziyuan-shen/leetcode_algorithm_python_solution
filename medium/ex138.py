"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        head_copied = Node(x = head.val)
        p1 = head.next
        p2 = head_copied
        while p1 != None:
            p2.next = Node(x = p1.val)
            p1 = p1.next
            p2 = p2.next
        p1 = head
        p2 = head_copied
        while p1 != None:
            p3 = head
            p4 = head_copied
            while p1.random != p3 and p3 != None:
                p3 = p3.next
                p4 = p4.next
            p2.random = p4
            p1 = p1.next
            p2 = p2.next
        return head_copied