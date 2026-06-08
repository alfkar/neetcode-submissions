# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reversed_list = None
        while head:
                nextNode = head.next
                head.next = reversed_list
                reversed_list = head
                head = nextNode
        index = 1
        head = None
        while reversed_list:
                if index == n:
                    reversed_list = reversed_list.next
                else:
                    nextNode = reversed_list.next
                    reversed_list.next = head
                    head = reversed_list
                    reversed_list = nextNode
                index+=1
        return head

