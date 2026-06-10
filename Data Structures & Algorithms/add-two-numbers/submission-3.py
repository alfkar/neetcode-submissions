# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        tail = None
        carry = 0
        if not l1:
            return l2
        if not l2:
            return l1
        while l1 or l2:
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
            if tail:
                tail.next = newNode
            else:
                result.next = newNode
            tail = newNode 
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            tail.next = ListNode(1, None)
        return result.next