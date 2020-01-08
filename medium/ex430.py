"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        p = head
        while p and not p.child:
            p = p.next
        if not p:
            return head
        else:
            next_level = p.child
            self.flatten(next_level)
            p.child = None
            remaining = p.next
            p.next = next_level
            next_level.prev = p
            if remaining:
                while p.next:
                    p = p.next
                p.next = remaining
                remaining.prev = p
            return head