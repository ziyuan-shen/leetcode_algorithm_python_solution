# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cout, digit = (l1.val+l2.val)//10, (l1.val+l2.val)%10
        added = ListNode(digit)
        pointer = added
        pointer1 = l1.next
        pointer2 = l2.next
        while not (pointer1==None and pointer2==None and cout==0):
            if pointer1 == None and pointer2 == None:
                if cout != 0:
                    pointer.next = ListNode(cout)
                    cout = 0
            elif pointer1 == None:
                cout, digit = (pointer2.val+cout)//10, (pointer2.val+cout)%10
                pointer.next = ListNode(digit)
                pointer2 = pointer2.next
            elif pointer2 == None:
                cout, digit = (pointer1.val+cout)//10, (pointer1.val+cout)%10
                pointer.next = ListNode(digit)
                pointer1 = pointer1.next
            else:
                cout, digit = (pointer1.val+pointer2.val+cout)//10, (pointer1.val+pointer2.val+cout)%10
                pointer.next = ListNode(digit)
                pointer1, pointer2 = pointer1.next, pointer2.next
            pointer = pointer.next
        return added