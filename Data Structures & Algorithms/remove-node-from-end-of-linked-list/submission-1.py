# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1=head
        p2=head
        prev=None
        for i in range(n-1):
            p2=p2.next
        while p2.next!=None:
            p2=p2.next
            prev=p1
            p1=p1.next
        
        if prev!=None:
            prev.next=p1.next
        else:
            head=head.next

        return head
        
        