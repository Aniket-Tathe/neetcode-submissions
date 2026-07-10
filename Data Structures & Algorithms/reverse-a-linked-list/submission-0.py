# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # first we build the linked list then we reverse it

        # for c in range(len(list(head))):
        #     if c ==0:
        #         tmp=ListNode(head[c])
        #     else:
        #         tmp=ListNode(head[c])
        #         tmp[c-1].next=head[c]
        # remember linkedlist is not iterable like array.

        # curr=head # remember this is ListNode head is a node, a node has two things: val and pointer to next node

        # while (curr!=None):
            # print(curr.val) # print what is at current position
            # curr=curr.next # move to next position so now curr is next node 
        
        # now to traverse and reverse:
        # we need three pointers curr=current, prev=store prev, nxt=to store tmp when we switch the pointers and also shift to next
        curr=head
        prev=None 

        while curr!=None:
            nxt=curr.next # stored the next otherwise if we directly change arrow i.e below code the next node and rest linkedlist lost coz pointer ch save nai kela
            curr.next=prev # current cha pointer point at prev i.e -> becomes <-
            prev=curr # now we shift, current becomes our prev for next iteration
            curr=nxt # nxt becomes our current for next iteration
        
# remember always visualize the linked list for eg: [1,2,3] like in ur head like ->1 -> 2-> 3-> notice the ->

        return prev # we return prev coz prev has the last value which is not null so our curr before becoming null the value we stored in prev so that becomes our new head