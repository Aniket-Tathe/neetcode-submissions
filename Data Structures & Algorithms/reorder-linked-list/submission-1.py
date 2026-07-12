# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        curr=head
        runner=head # we move this till one

        while curr and curr.next and curr.next.next: # also imp
            runner=curr # very imp otherwise crash on later iteration see jupyter
            # we moving runner each iteration ahead 
            while runner.next.next != None: # we want to do runner.next=nxt but if we naively run while runner.next is not None: 
                # runner will go till None and then None.next is error we want to stop one value before None hence we run runner.next.next
                # if we have [1,2,3,4] we are stopping at 3 as 3.next=4 and 3.next.next=None
                runner=runner.next

            last=runner.next # we save 4 otherwise we'll lose it it we change pointers before
            runner.next= None # we make 3->4->None to 3-> None
            # curr.next=last # connect 1 to 4
            # last.next=curr.next.next # connect 4 to 2 (i.e 1.next.next as we joined 4 above so just curr.next=4)
            # above two lines broke the 1,2,3,4 to 1,4,None and 2,3,None coz once we joined 1 to 4 1.next.next is now None and not 2
            # see jupyter for more details  

            # first we connect 4-> None to 4->2
            last.next=curr.next # (4.next = 1.next i.e 2)
            # now we do 1 connect to 4
            curr.next=last # now we have 1,4,2,3

            # advance curr to next for next iteration
            curr=last.next # we go 4.next so at 2
# no return here coz you rearranged the list , also above is O(n2)

# neetcode soln: O(n) time and O(1) memory
# fast and slow pointers to find middle: eg: 1->2->3->4 s=1, f=s+2 as f.next=None we say s=middle and cut after that
# in two halves then reverse the pointers of other half and add one by one in first half
# for odd: 1->2->3->4->5->None when f is at none i.e s will be at 3. s.next = second half
# watch video for visual explanation
# remember whenever u break the links / pointers make sure to save somewhere the after portion of broken otherwise lost
# no return as we are modifying the list we are given 

        # slow,fast=head,head.next

        # while fast and fast.next: # i.e while both are not None we keep going
        #     slow=slow.next # not slow=head.next as head is fixed head.next =same for each iteration so infinite loop
        #     fast=fast.next.next # not fast=head.next otherwise each loop we will be just iterating over same value

        # # this will give us fast and slow we find middle
        # # now we reverse the second half
        # second=slow.next # second half of the list  1->2->3->4->None became 1->2 and 3->4->None
        # slow.next= None # 1->2->None treat both list as independant
        # prev=None # same as slow.next

        # # reverse second half
        # while second:
        #     # we have 3->4->None we want to reverse it None<-4<-3
        #     tmp=second.next # save 3.next i.e 4 and remaining list in tmp
        #     second.next=prev # revere the pointer point it to None
        #     # now for next iteration we move forward the pointers
        #     prev=second 
        #     # second=second.next wrong as second.next is now None , not 4 as we updated it above
        #     second=tmp # thats why we stored it in tmp so we can continue now we move to 3.next=4 i.e tmp=4

        # # now we rearrange and merge:
        # # when above loop finished second=None and prev=Last value i.e 4 in  3<-4<-None
        # second = prev # last non zero value
        # first=head # leftmost portion of first list

        # while second: # as we want to fill second half in first so until it has values
        #     tmp1=first.next # we save the first.next list somewhere
        #     tmp2=second.next # we save the second list 

        #     first.next =second # join 1 to 4
        #     second.next=tmp1 # join to first half

        #     # moving for next iteration
        #     first=tmp1 # move ahead in first list
        #     second=tmp2 # move ahead in second list


