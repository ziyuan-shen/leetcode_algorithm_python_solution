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
        visited = {head:head_copied}
        p1 = head
        p2 = head_copied
        while p1 != None:
            if p1.next not in visited:
                if p1.next == None:
                    p2.next = None
                else:
                    visited[p1.next] = Node(x = p1.next.val)
                    p2.next = visited[p1.next]
            else:
                p2.next = visited[p1.next]
            if p1.random not in visited:
                if p1.random == None:
                    p2.random = None
                else:
                    visited[p1.random] = Node(x = p1.random.val)
                    p2.random = visited[p1.random]
            else:
                p2.random = visited[p1.random]
            p1 = p1.next
            p2 = p2.next
        return head_copied