class Node:

    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.next=self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.cap=capacity
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self,node):
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev
    
    def insert(self,node):
        prev=self.right.prev
        prev.next=node
        self.right.prev=node
        node.prev=prev
        node.next=self.right
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
