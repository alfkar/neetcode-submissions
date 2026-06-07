class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        visited = {}
        index = 0
        length = -1
        while head is not None:
            visited[index] = head
            head = head.next
            length += 1
            index += 1
        dummyNode = ListNode()
        result = dummyNode
        half = math.ceil(length/2)
        for n in range(0, math.ceil(length/2)+1):
            if n == math.ceil(length/2):
                result.next = visited[n]
                result = visited[n]
                result.next = None
                break
            result.next = visited[n]
            result = result.next
            result.next = visited[length-n]
            result = result.next
        return None