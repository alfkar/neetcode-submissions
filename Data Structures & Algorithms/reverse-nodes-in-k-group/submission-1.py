# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        resultHead = None
        count = 0
        currentReverse = None
        prevTail = head
        currTail = None
        while head:
            if count != k:
                nextNode = head.next           
                head.next = currentReverse
                currentReverse = head
                if count == 0:
                    currTail = head
                head = nextNode
                count += 1
            if count == k:
                if not resultHead:
                    resultHead = currentReverse
                    prevTail = currTail
                    currentReverse = None
                else: 
                    prevTail.next = currentReverse
                    prevTail = currTail
                    currentReverse = None 
                count = 0
        rCount = 0
        revLast = None
        while rCount < count:
            nextNode = currentReverse.next
            currentReverse.next = revLast
            revLast = currentReverse
            currentReverse = nextNode
            rCount +=1    
        if resultHead is None:
            return revLast
        else:
            prevTail.next = revLast
            return resultHead