# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head==None:
            return
        middle=head
        tail=head
        while tail and tail.next:
            tail=tail.next.next
            middle=middle.next

        second=middle.next
        middle.next=None

        prev=None
        current=second

        while current!=None:
            after=current.next
            current.next=prev
            prev=current
            current=after
        
        first=head
        second=prev

        while first!=None and second!=None:
            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1

            first=temp1
            second=temp2


        
        




        

