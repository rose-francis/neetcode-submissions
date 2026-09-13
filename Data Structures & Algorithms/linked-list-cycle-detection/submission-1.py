# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head

        while True:
            if fast==None:
                return False

            slow=slow.next
            if fast.next!=None:
                fast=fast.next.next
            else:
                return False
            
            if slow==fast:
                return True

        