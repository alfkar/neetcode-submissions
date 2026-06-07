# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val =  val
        self.next = next
        self.index = -1

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        index = 0
        if not head:
            return False
        while head.next is not None:
            head.index = index
            visited[index] = head
            if head.next.index in visited:
                return True
            head = head.next
            index += 1
        return False