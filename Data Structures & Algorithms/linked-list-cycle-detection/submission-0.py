# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        pointers=set()
        current=head
        while True:
            if current==None:
                return False
            elif current in pointers:
                return True
            pointers.add(current)
            current=current.next
        