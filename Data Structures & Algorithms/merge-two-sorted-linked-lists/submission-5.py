class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        if list1 is None and list2 is None:
            return list1
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        tail = head
        while list1 is not None or list2 is not None:
            if list2 is None:
                tail.next = list1
                tail = list1
                list1 = list1.next
            elif list1 is None:
                tail.next = list2
                tail = list2
                list2 = list2.next
            elif list1.val <= list2.val:
                tail.next = list1
                tail = list1
                list1 = list1.next
            elif list1.val > list2.val:
                tail.next = list2
                tail = list2
                list2 = list2.next
        return head