class ListNode:
    def __init__(self, val=0,key=-1, next=None, prev=None):
        self.val =  val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.LRU = self.head
    def get(self, key: int) -> int:
        isCached = self.cache.get(key, -1)
        if isCached == -1:
            return isCached
        if self.LRU == isCached:
            return isCached.val
        else:
            isCached.prev.next = isCached.next
            if isCached.next:
                isCached.next.prev = isCached.prev
            self.LRU.next = isCached
            isCached.prev = self.LRU
            isCached.next = None
            self.LRU = isCached
            return isCached.val

    def put(self, key: int, value: int) -> None:
        isCached = self.cache.get(key, None)
        if self.LRU == isCached:
            isCached.val = value
            return None
        if isCached:
            isCached.val = value
            isCached.prev.next = isCached.next
            if isCached.next:
                isCached.next.prev = isCached.prev
            self.LRU.next = isCached
            isCached.prev = self.LRU
            isCached.next = None
            self.LRU = isCached
            return None
        newEntry = ListNode(value,key,None,self.LRU) 
        self.LRU.next = newEntry 
        self.cache[key] = newEntry
        self.LRU = self.LRU.next
        if len(self.cache) > self.capacity:
            if self.head.next:
                del self.cache[self.head.next.key]
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
        return None