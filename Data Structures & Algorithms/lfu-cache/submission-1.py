class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.freq=1
        self.prev=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        self.size=0

    def length(self):
        return self.size

    def pushRight(self, node):
        prev=self.right.prev
        prev.next=node
        self.right.prev=node
        node.prev=prev
        node.next=self.right
        self.size+=1
        
    def pop(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        node.prev=node.next=None
        self.size-=1
    
    def popLeft(self):
        if self.length()==0:
            return None
        node=self.left.next
        self.pop(node)
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.nodeMap={} # key ->node
        self.countMap=defaultdict(LinkedList) #count -> DLL of nodes
        self.lfuCount=0
    
    def counter(self,node):
        count=node.freq
        self.countMap[count].pop(node)
        if self.lfuCount==count and self.countMap[count].length()==0:
            self.lfuCount+=1
        node.freq+=1
        self.countMap[node.freq].pushRight(node)

    def get(self,key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node=self.nodeMap[key]
        self.counter(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if self.cap==0:
            return
        
        if key in self.nodeMap:
            node=self.nodeMap[key]
            node.val=value
            self.counter(node)
            return
        
        if len(self.nodeMap)==self.cap:
            node=self.countMap[self.lfuCount].popLeft()
            self.nodeMap.pop(node.key)
        
        node=Node(key,value)
        self.nodeMap[key]=node
        self.countMap[1].pushRight(node)
        self.lfuCount=1
  



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)