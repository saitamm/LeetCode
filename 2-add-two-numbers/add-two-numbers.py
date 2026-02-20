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
        while l1 and l2:
            number = l1.val + l2.val + rang
            newNode = ListNode(number  % 10)
            head.next = newNode
            head = head.next
            rang = number / 10
            l1 = l1.next
            l2 = l2.next
        while l1 :
            number = l1.val + rang
            newNode = ListNode(number  % 10)
            head.next = newNode
            head = head.next
            rang = number / 10
            l1 = l1.next
        while l2 :
            number = l2.val + rang
            newNode = ListNode(number  % 10)
            head.next = newNode
            head = head.next
            rang = number / 10
            l2 = l2.next
        print(rang)
        if (rang):
            newNode = ListNode(rang)
            head.next = newNode
            head = head.next
        return(result)