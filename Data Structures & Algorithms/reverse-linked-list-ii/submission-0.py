# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        
        start=head
        if left!=1:
            for _ in range(left-2):
                start=start.next
            temp=start
            start=start.next
            temp.next=None

        end=start
        for _ in range(right-left):
            end=end.next
        if end.next!=None:
            after_end=end.next
            end.next=None
        else:
            after_end=None
        
        prev=None
        current=start
        while current!=None:
            after=current.next
            current.next=prev
            prev=current
            current=after
        end=start
        start=prev
        if left==1:
            head=start
        else:
            temp.next=start
        if after_end:
            end.next=after_end
        return head


    

    
         


        

        
            
        