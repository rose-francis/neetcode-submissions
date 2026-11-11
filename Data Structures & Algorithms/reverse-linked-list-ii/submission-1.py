# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if left!=1:
            before=head
            for _ in range(left-2):
                before=before.next
            l=before.next
        else:
            l=head

        r=l
        for _ in range(right-left):
            r=r.next
        after=r.next

        prev=None
        cur=l
        for _ in range(right-left+1):
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        
        if left!=1:
            before.next=prev
        l.next=after

        if left==1:
            return r
        else:
            return head
        