# Definition for singly-linked list.
# very sexy question, combines two pointers plus linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
    #     curr=head
    #     prev=None

    #     while curr:
    #         tmp=curr.next
    #         curr.next=prev
    #         prev=curr
    #         curr=tmp
        
    #     # made few mistakes read the jupyter 
    #     # 1,2,3,4
    #     # for eg: how to remove one element 
    #     # prev is our end head from where we start
    #     # dummy=ListNode(0)
    #     # dummy.next=prev # becomes 1<-2<-3<-4<-0 
    #     # p=dummy
    #     # p.next=p.next.next # becomes 1<-2<-3<-0

    #     # dummy.next # gives 1<-2<-3

    #     i=1

    #     dummy=ListNode(0)
    #     dummy.next=prev
    #     # anchor=ListNode(0)
    #     # anchor.next=prev
    #     anchor=dummy
    

    #     while i<=n:
    #         if i!=n:
    #             prev=prev.next
    #             dummy=dummy.next
    #         else: # 1<-2<-3<-4<-0 
    #             tmp=prev.next # 1<-2<- saved
    #             dummy.next=tmp # # 1<-2<-4<-0
    #         i+=1

    # # now we re reverse we have 1<-2<-4<-0
    #     print(dummy.val) # need one walker and one anchor 
    #     # anchor stays fixed and walker walks 
    #     # print(anchor.next.val)
    #     curr=anchor.next # gives us 1<-2<-4 , if u do dummy case 2 fails coz 
    #     # print(curr.val)
    #     prev=None

    #     while curr:
    #         tmp=curr.next # store  1<-2
    #         curr.next=prev
    #         prev=curr
    #         curr=tmp

    #     return prev

#### neetcode soln 
# u have 5 elements u wnt to remove 2nd from last i.e is just 5-2 = 3 from the start
# 1,2,3,4,5 so n=2, from behind i.e u want to remove 4 
# so u traverse till 3 then just do maybe 3.next= 3.next.next and 4th is just skipped
# The catch is where 5 comes from. You have to walk the whole list once to count L, then walk again to position 3. That's 2 passes. It's still
#   O(n) and much simpler than reversing twice.

# one pass soln: n + 1
# very sexy question, combines two pointers plus linked list.
# have 2 pointers
# i.e 1->2->3->4 , n= 2 and we do l,r pointer at 1, we move move l-r=n, and then let r move to end our l will end up on node which we want to delete i.e 3 but we want one before to do like 2.next = 2.next.next so 3 is skipped. so we introduce l pointer at dummy node 0
# so 0->1->2->3->4 now l is at 0 and r same, now we end up on 2 and do 2.next=2.next.next

        l=ListNode(0,head) # val=0, .next =head
        # l.next=head because u did above = head
        head_curr=l # coz case 2 madhe head ch remove hotay 
        r=head
        i=0

        while r!=None:
            if i<n:
                r=r.next
                i+=1
            else:
                r=r.next
                l=l.next
        
        l.next=l.next.next # here we skip the number which we want to skip

        
        # return head # problem with this is when we pop the first head itself then head we need to shift, case 2 fail hote

        return head_curr.next  # coz head is 0 u want 0 nantr cha hence head.next
# [1], n=1:        0 → None        head_curr.next = None     → []     ✅
#   [1,2], n=2:      0 → 2           head_curr.next = 2        → [2]    ✅
#   [1,2,3,4,5], 2:  0 → 1 → 2 → 3 → 5   head_curr.next = 1    → [1,2,3,5] ✅

## neetcode soln:
# two pointers but n la kami kar

        # dummy = ListNode(0, head)
        # left = dummy
        # right = head

        # while n > 0:
        #     right = right.next
        #     n -= 1

        # while right:
        #     left = left.next
        #     right = right.next

        # left.next = left.next.next
        # return dummy.next