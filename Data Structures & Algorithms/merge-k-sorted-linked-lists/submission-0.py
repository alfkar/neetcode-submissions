
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        loopCon = True
        numNonEmpty = 0
        dummy = ListNode(0,None)
        head = dummy
        if not lists:
            return head.next
        while loopCon:
            index = 0
            for i, l in enumerate(lists):
                if not l:
                    continue
                numNonEmpty += 1
                if not lists[index]:
                    index = i
                    continue
                if l.val <= lists[index].val:
                    index = i
            head.next = lists[index]
            head = head.next
            lists[index] = lists[index].next
            if numNonEmpty == 1:
                for l in lists:
                    if l:
                        head.next = l
                break
            numNonEmpty = 0
        return dummy.next