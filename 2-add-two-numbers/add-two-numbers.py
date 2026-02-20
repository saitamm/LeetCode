# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0):

        # 1️⃣ Base case
        if not l1 and not l2 and carry == 0:
            return None

        # 2️⃣ Get values safely
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # 3️⃣ Compute total
        total = val1 + val2 + carry

        # 4️⃣ Create current node
        node = ListNode(total % 10)

        # 5️⃣ Recursive call for next
        node.next = self.addTwoNumbers(
            l1.next if l1 else None,
            l2.next if l2 else None,
            total // 10
        )

        return node