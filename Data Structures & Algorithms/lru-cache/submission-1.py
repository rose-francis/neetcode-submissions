class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key=key
        self.val=val
        self.next=next
        self.prev=prev

class LRUCache:
    def __init__(self, capacity: int):
        self.cache={}
        self.head=None
        self.tail=None
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            if node==self.tail:
                return node.val
            if node==self.head:
                self.head=self.head.next
            if node.prev:
                node.prev.next=node.next
            if node.next:
                node.next.prev=node.prev
            node.next=None
            node.prev=self.tail
            self.tail.next=node
            self.tail=node
            return node.val

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            if node!=self.tail:
                if node==self.head:
                    self.head=self.head.next
                if node.prev:
                    node.prev.next=node.next
                if node.next:
                    node.next.prev=node.prev
                self.tail.next=node
                node.next=None
                node.prev=self.tail
                self.tail=node
        else:
            node=Node(key,value)
            if not self.head:
                self.head=node
                self.tail=node
            else:
                node.prev=self.tail
                self.tail.next=node
                self.tail=node
            self.cache[key]=node
            
            if len(self.cache)>self.capacity:
                k=self.head.key
                del self.cache[k]
                self.head=self.head.next
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)