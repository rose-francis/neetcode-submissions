# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=head
        for _ in range(n):
            fast=fast.next

        slow=head
        if fast==None:
            head=head.next
            return head
        while fast.next:
            fast=fast.next
            slow=slow.next
        
        temp=slow.next
        slow.next=temp.next


        return head

        
        