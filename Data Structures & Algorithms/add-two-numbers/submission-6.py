# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        tail = result
        carry = 0
        while l1 or l2 or carry:
            l1val = 0
            l2val = 0
            if l1:
                l1val = l1.val
            if l2:
                l2val = l2.val
            valSum = l1val + l2val + carry
            carry = 0
            if valSum > 9:
                carry = 1
                valSum -= 10
            newNode = ListNode(valSum, None)
            tail.next = newNode
            tail = newNode 
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result.next