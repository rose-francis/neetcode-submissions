# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        cur1=list1
        cur2=list2

        dummy=ListNode(0,None)
        cur=dummy
        while cur1!=None and cur2!=None:
            if cur1.val>=cur2.val:
                cur.next=cur2
                cur2=cur2.next
                cur=cur.next
            else:
                cur.next=cur1
                cur1=cur1.next
                cur=cur.next
        
        if cur1!=None:
            cur.next=cur1
        
        if cur2!=None:
            cur.next=cur2
        
        return dummy.next