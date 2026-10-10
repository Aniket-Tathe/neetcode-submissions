class MedianFinder:

#     def __init__(self):
#         self.median = []

#     def addNum(self, num: int) -> None:
#         # if num:
#         self.median.append(num)
        

#     def findMedian(self) -> float:
#         self.median.sort()
#         n=len(self.median)
#         if n % 2 !=0:
#             # return sum(self.median)/len(self.median)
#             return self.median[n//2]
#         else:
#             return (self.median[(n // 2)-1] + self.median[n//2])/2

# above is brute force time complexity is O(1) for addnum and O(nlogn) for findmedian for sorting it is logn and other part is n so total nlogn

# neetcode soln
# A heap is a list that always keeps its smallest item at index 0. Adding and removing take O(log n), and peeking at the smallest is O(1).
# heap = priority queue
# we gonna have 2 heaps one will be small and other big, and small <= big always. size of both approx same in each stage with max diff between them as 1
# heap is just an array or list only diff is we dont add at beginning or at the end, we just add, and always it will be O(logn), removing also O(logn).
# two types of heaps are there: max heap, where findmax will always be a O(1) operation in normal list it would be O(n) as u traverse whole list 
# and min heap, where findmin will be O(1)
# here we will have the small heap as max heap, and bigger heap as min heap. so median will be smaller cha max i.e last value if odd, bagh kuthla heap bigger aahe if small mag last value ghe ani if big then first value ghe

# heap defn : A heap is a specialized, tree-based data structure that is shaped like a complete binary tree and satisfies the heap property
# The Heap Property: The relationship between parent and child nodes determines the type of heap:
# • Max-Heap: The value of every parent node is greater than or equal to the values of its children, meaning the largest value is always at the root (the top).
# • Min-Heap: The value of every parent node is less than or equal to the values of its children, meaning the smallest value is always at the root
# lookup i.e min or max lookup is O(1), extract / delete / insert is O(logn)

    def __init__(self):
        # two heaps, small max heap and bigger min heap
        self.small,self.large=[],[]

    def addNum(self, num: int) -> None:        
        heapq.heappush(self.small,num*-1) # in python u can only implement min heap for some reason so to make this min heap max, we do num*-1. as 1<2<3 but -1>-2>-3 so its stored as -3<-2<-1

        # make sure every num is <= in the small heap as comp to bigger heap, if not shift
        if (self.small and self.large # i.e if small and large exists 
        and (-1*self.small[0]) > self.large[0]): # some nos in smaller> bigger then we push to bigger  
        # (-1*self.small[0]) coz example u get -3 out the real val is 3 so -1*-3 = 3
            val=-1*heapq.heappop(self.small) # pop the val from small which is > then shift
            heapq.heappush(self.large,val) 

        # now for the uneven size we want it approx equal or max diff to be 1, if not then shift
        if len(self.small) > len(self.large)  + 1 : # i.e size > 1 like 2 or more
            # i.e small madhe ek value  jast aahe so we pop and put val in large
            val=-1*heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        # agar ulta asen:
        if len(self.small) + 1 < len(self.large): # i.e size > 1 like 2 or more
            # i.e small madhe ek value  jast aahe so we pop and put val in large
            val=heapq.heappop(self.large)
            heapq.heappush(self.small,-1*val)
        # all these are logn operations
        
    def findMedian(self) -> float:
        # odd length
        if len(self.small)> len(self.large):
            return -1*self.small[0] # means like [-3,-2,-1] [4,5] we return small[0]*-1 i.e 3

        # reverse 
        if len(self.small)< len(self.large):
            return self.large[0] # means like [-3,-2,-1] [4,5] we return small[0]*-1 i.e 3

        # if even, we return mean
        if len(self.small) == len(self.large):
            return ((-1*self.small[0]) + (self.large[0]))/2