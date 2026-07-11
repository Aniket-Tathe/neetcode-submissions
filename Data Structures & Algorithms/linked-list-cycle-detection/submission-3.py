# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        hashmap={} # counting the occurences

        while head is not None:
            value=head.val
            hashmap[value]=hashmap.get(value,0)+1

            if 10 in hashmap.values(): # jugaad try to find anything more than 10 repeating, as if repeats there [1,2,1] just asking if 2 in values will return wrong
                print("looping") # if any value >10 in counts means yes it repeated
                return True

            head=head.next # move to next node 

        return False

# neetcode soln: Floyd's Tortoise and Hare
# have a slow and fast pointer: s and f where f=s+1 
# so basically we doing curr.next and curr.next.next and if there is a cycle these two would be equal then we return True 
# see video v.imp always O(n) above s and f why see video how f catches up to s

        slow,fast=head,head

        while fast and fast.next: # coz fast will reach null (if there is null) faster as its +1 of slow so we write while loop wrt to f
            slow=slow.next
            fast=fast.next.next

            if slow==fast: # i.e found the cycle
                return True 

        return False # if above while loop breaks means no cycle


