class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        firstList = True
        head = ListNode()
        if list1 is None and list2 is None:
            return list1
        elif list1 is None:
            head = list2
            list2 = list2.next
        elif list2 is None:
            head = list1
            list1 = list1.next
        elif list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        prevValue = ListNode()
        while list1 is not None or list2 is not None:
            if list2 is None:
                if firstList:
                    head.next = list1
                    prevValue = list1
                    list1 = list1.next
                    firstList = False
                else: 
                    prevValue.next = list1
                    prevValue = list1
                    list1 = list1.next
            elif list1 is None:
                if firstList:
                    head.next = list2
                    prevValue = list2
                    list2 = list2.next
                    firstList = False
                else:
                    prevValue.next = list2
                    prevValue = list2
                    list2 = list2.next
            elif list1.val <= list2.val:
                if firstList:
                    head.next = list1
                    prevValue = list1
                    list1 = list1.next
                    firstList = False
                else:
                    prevValue.next = list1
                    prevValue = list1
                    list1 = list1.next
            elif list1.val > list2.val:
                if firstList:
                    head.next = list2
                    prevValue = list2
                    list2 = list2.next
                    firstList = False
                else:
                    prevValue.next = list2
                    prevValue = list2
                    list2 = list2.next
        return head