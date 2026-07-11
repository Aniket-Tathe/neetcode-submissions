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
                print("looping") # if any value >1 in counts means yes it repeated
                return True

            head=head.next # move to next node 

        return False