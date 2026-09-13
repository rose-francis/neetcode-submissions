# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(0)
        current=head
        carry=0
        while  l1!=None and l2!=None:
            summ=l1.val+l2.val+carry
            res=summ%10
            carry=summ//10
            new=ListNode(res)
            current.next=new
            current=current.next
            l1=l1.next
            l2=l2.next
        
        while l1!=None:
            summ=l1.val+carry
            res=summ%10
            carry=summ//10
            new=ListNode(res)
            current.next=new
            current=current.next
            l1=l1.next

        while l2!=None:
            summ=l2.val+carry
            res=summ%10
            carry=summ//10
            new=ListNode(res)
            current.next=new
            current=current.next
            l2=l2.next

        if carry!=0:
            new=ListNode(carry)
            current.next=new

        return head.next
        

        


