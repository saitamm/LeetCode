# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode((l1.val+l2.val)%10)
        rang = (l1.val+l2.val)/10
        l1 = l1.next
        l2 = l2.next
        head = result
        while l1 or l2 or rang:
            number1 = l1.val if l1 else 0
            number2 = l2.val if l2 else 0
            number = number1 + number2 + rang
            newNode = ListNode(number  % 10)
            head.next = newNode
            head = head.next
            rang = number / 10
            if l1 :
                l1 = l1.next
            if l2 :
                l2 = l2.next
        return(result)