
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        temp=head
        
        while list1!=None and list2!=None:
            if list1.val<list2.val:
                new=ListNode(list1.val)
                temp.next=new
                list1=list1.next
                temp=temp.next
                
            elif list1.val>list2.val:
                new=ListNode(list2.val)
                temp.next=new
                list2=list2.next
                temp=temp.next
            
            else:
                for _ in range(2):
                    new=ListNode(list1.val)
                    temp.next=new
                    temp=temp.next
                list1=list1.next
                list2=list2.next

        
        while list1!=None:
            new=ListNode(list1.val)
            temp.next=new
            temp=temp.next
            list1=list1.next
        
        while list2!=None:
            new=ListNode(list2.val)
            temp.next=new
            temp=temp.next
            list2=list2.next
        
        return head.next
