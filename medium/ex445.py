# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = l1.val
        num2 = l2.val
        while l1.next:
            l1 = l1.next
            num1 = num1 * 10 + l1.val
        while l2.next:
            l2 = l2.next
            num2 = num2 * 10 + l2.val
        num = num1 + num2
        digits = [int(d) for d in list(str(num))]
        ans = ListNode(digits[0])
        p = ans
        for i in range(1, len(digits)):
            p.next = ListNode(digits[i])
            p = p.next
        return ans