"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        if head.next == head:
            head.next = Node(insertVal)
            head.next.next = head
            return head
        p = head
        while p.next.val >= p.val:
            p = p.next
            if p == head:
                break
        if insertVal < p.val:
            while insertVal > p.next.val:
                p = p.next
        temp = p.next
        p.next = Node(insertVal)
        p.next.next = temp
        return head