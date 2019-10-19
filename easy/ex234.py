# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head==None:
            return True
        reverse_list = []
        current_node = head
        while current_node != None:
            reverse_list.insert(0, current_node.val)
            current_node = current_node.next
        current_node = head
        for i in range(len(reverse_list)):
            if reverse_list[i] != current_node.val:
                return False
            current_node = current_node.next
        return True