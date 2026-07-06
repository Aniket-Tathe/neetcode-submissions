class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
        # for optimal soln: 
        # set() is no dupliactes so it auto handles case where we have duplicates
        # set is not sorted rem. it may look like but not necessary
        # nums_set=set(nums)
        # print(nums_set)
        # longest=0

        # for i in range(0,len(nums)):
        #     local_max=0
        #     if nums[i]-1 not in nums_set: 
        #         local_max=1
        #         local_num=nums[i]
        #         while local_num+1 in nums_set:
        #             local_max+=1
        #             local_num+=1
        #         if longest<local_max:
        #             longest=local_max
        # return longest

# neetcode soln:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0

        for n in nums:
            # check if its the start of sequence
            if (n-1) not in numset: #means its a start
                length=0
                while (n+length) in numset:
                    length +=1
                longest=max(length,longest)
        return longest
            
        