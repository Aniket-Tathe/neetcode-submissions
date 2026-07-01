# class Solution: # brute force
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i!=j and nums[i]+nums[j]==target:
#                     return [i,j]

class Solution: # hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
    
        for idx,value in enumerate(nums): # u get index ani value donhi
            need= target - value # nums0+nums1=7 hence num1=7-num0
            if need in hashmap: # agar aahe tar return kar nahitr add to the hashset
                return [hashmap[need],idx]
            hashmap[value]=idx
