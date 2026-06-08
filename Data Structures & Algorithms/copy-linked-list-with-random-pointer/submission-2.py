"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        visited_to_index = {}
        index_to_visited = {}
        index = 0
        dummy = Node(-1,head, None)
        if not head:
            return head
        while head:
            visited_to_index[head] = index
            index_to_visited[index]=Node(head.val, head.next, head.random)
            head = head.next
            index +=1
        head = dummy.next
        while head:
            index = visited_to_index[head]
            currentNode = index_to_visited[index]
            currentNode.next = index_to_visited.get(index+1, None)
            currentNode.random = index_to_visited.get(visited_to_index.get(head.random, None), None)
            head = head.next
        return index_to_visited[0]          

        
        