class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.counter=1
        self.next=None
        self.prev=None

class LFUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    def remove(self,node):
        prev=node.prev
        next=node.next
        prev.next,next.prev=next,prev

    def insert(self,node):
        prev=self.right.prev
        prev.next=node
        self.right.prev=node
        node.prev=prev
        node.next=self.right
        
    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        self.cache[key].counter+=1
        if self.right.prev!=self.cache[key]:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if self.cap==0:
            return
        if key in self.cache:
            self.cache[key].counter+=1
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].val=value
            return
        
        if len(self.cache)<self.cap:
            self.cache[key]=Node(key,value)
            self.insert(self.cache[key])
        else:
            min_frq=float('inf')
            min_k=None
            temp=self.left.next
            while temp!=self.right:
                if temp.counter<min_frq:
                    min_frq=temp.counter
                    min_k=temp.key
                temp=temp.next
            if min_k is not None:
                self.remove(self.cache[min_k])
                del self.cache[min_k]
                self.cache[key]=Node(key,value)
                self.insert(self.cache[key])

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)