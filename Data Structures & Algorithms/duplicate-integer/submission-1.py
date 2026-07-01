# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         o=[]
#         for i in range(len(nums)):
#             print(i,"from i")
#             for j in range(len(nums)):
#                 print(j, "from j")
#                 if j!=i:
#                     if nums[j]==nums[i]:
#                         o.append(1)
#         if len(o) != 0:
#             return True
#         else:
#             return False

# class Solution:
#     def hasDuplicate(self,nums):
#         for i in range(i+1,len(nums)): # hagla ithe
#             if nums[i]==nums[i+1]:
#                 return True 
#         return False  

# try set:
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         seen=set()
#         for i in range(len(nums)):
#             if nums[i] in seen:
#                 return True
#             else:
#                 seen.add(nums[i])
#         return False

# using sorting: coz mag duplicates will be adjacent so you just check neighbours,
# but remember where the list ends 
class Solution: # kind of two pointers
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_list=sorted(nums)
        p1=0
        for i in range(1,len(nums)):
            if sorted_list[p1]==sorted_list[i]:
                return True
            else:
                p1+=1
        return False

# for counting the duplicates:
# hashmap 

# class Solution:
#     def countduplicates(self,nums):
#         hashmap={}
#         for i in nums:
#             if i in hashmap:
#                 hashmap[i]+=1
#             else:
#                 hashmap[i]=1
#         return hashmap

# class Solution: # build the hashmap which has nums and their count and from that get duplicates
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         hashmap={}
#         for i in nums:
#             if i in hashmap:
#                 hashmap[i]+=1
#             else:
#                 hashmap[i]=1
#         # for i in nums:
#         #     if hashmap[i] != 1:
#                 # return True

#         # or using .values() which gives u direct values
#         for value in hashmap.values():
#             if value !=1:
#                 return True
#         return False