# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode(0) # dummy list which we append
        tail=dummy # we need reallist at end 
        l1,l2=list1,list2

        while l1 and l2: # joh parynat doghan madhe None nahiye
            if l1.val <= l2.val: # handle both equal and == case
                tail.next=l1 # put that value in into tail
                l1=l1.next # l1 we shift to next
            else:
                tail.next=l2 # means l1>l2  
                l2=l2.next 
            # while building  .next on leftside curr.next= next node  
            # while traversing .next on right side curr=curr.next we move from curr to next node
        
            tail=tail.next # move tail to next 
# dummy is start 0 then we do tail=dummy then we build tail and append to tail
# so we are doing 0 (value from dummy and appending) 0->1->2->3 and so on
# in the return we do return dummy.next which will give us the cut version where we skip 0
# and we have already built 1->2->3 that we return

        tail.next = l1 or l2      # attach whichever list still has nodes and other is empty it falls out of while loop
        return dummy.next

    # neetcode soln: recursion
    
        