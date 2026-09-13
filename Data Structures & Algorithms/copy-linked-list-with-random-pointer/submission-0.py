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
        current=head
        head_new=None
        l=[]
        while current!=None:
            new=Node(current.val)
            if current.random==None:
                l.append([current.val,None])
            else:
                index=0
                temp=head
                while temp!=None and current.random!=temp:
                    temp=temp.next
                    index+=1
                if current.random==temp:
                    l.append([current.val,index])

            if head_new==None:
                head_new=new
                current_new=new
            else:
                current_new.next=new
                current_new=current_new.next
            current=current.next

        i=0
        current_new=head_new
        while current_new!=None:
            index=l[i][1]
            if index==None:
                current_new.random=None
            else:
                j=0
                temp=head_new
                while j!=index and temp!=None:
                    temp=temp.next
                    j+=1
                if j==index:
                    current_new.random=temp
            current_new=current_new.next
            i+=1

        return head_new







        