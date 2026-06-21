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
            # Move pointer from from prev -> current -> next to prev -> next
            isCached.prev.next = isCached.next
            if isCached.next:
                isCached.next.prev = isCached.prev
            # Set newly accessed entry to most recently used 
            self.LRU.next = isCached
            # Set newly accessed entry prev to tail of LRU
            isCached.prev = self.LRU
            isCached.next = None
            # Set LRU tail to newly accessed entry 
            self.LRU = isCached
            # Return accessed value
            return isCached.val

    def put(self, key: int, value: int) -> None:
        # New Entry
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
        # LRU linked list, new entry is most recently used
        self.LRU.next = newEntry 
        # Cache gets the new Entry
        self.cache[key] = newEntry
        # Set tail of LRU do the newly added element
        self.LRU = self.LRU.next
        # If cache exceeds capacity:
        if len(self.cache) > self.capacity:
            # if LRU has an element
            if self.head.next:
                # delete entry from cache
                del self.cache[self.head.next.key]
                # Remove head from linked list and get new head of list
                self.head.next = self.head.next.next
                # Set new prev of head to prev.head
                self.head.next.prev = self.head
        return None