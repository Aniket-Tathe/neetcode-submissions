class Solution:
    def findMin(self, nums: List[int]) -> int:
        # trivial soln but just O(n)

        # minnum=0

        # for i in range(len(nums)-1):
            # if nums[i]>nums[i+1]: 
                # minnum=nums[i+1] # [4, 5, 0, 1, 2, 3] look at 5  0   <- the ONE place where nums[i] > nums[i+1]  (the "drop"/pivot)
#               The minimum is the element right after that drop (0 here). Everywhere else it's ascending; the min is exactly where the ascending order breaks.
                # return minnum
        
        # binary search : first hint array sorted aahe second hint log(n) time
        # neetcode soln
        # if nums[mid] > nums[r] search right, else search left
        # / gives fraction // gives floor value division 10//3 is 3 and 10/3 is 3.3333

        res=nums[0]
        l=0
        r=len(nums)-1

        while l<=r: # <= not < 
            if nums[l]<nums[r]: # if fully sorted like full complete rotation kela ki left<right direct break
                res=min(res,nums[l])
                break # break the while loop
            
            # when its not fully rotated i.e left not less than right
            mid=(l+r)//2
            # print(mid)
            res=min(res,nums[mid]) # imp before shrinking you are saving, nahitr mid la num asen tar skip hou shakta when u do mid-1

            if nums[mid] >= nums[l]: # means its part of the left sorted side and we search right side
                # eg: 3,4,5,0,1  5>3 we go right side move l pointer
                # we move l to mid+1
                l=mid+1
            else: # mid < l  
                r=mid-1

        return res        
            

# if we want to use l<r

#   class Solution:
#       def findMin(self, nums: List[int]) -> int:
#           l, r = 0, len(nums) - 1
#           while l < r:                 # CHANGE 1
#               mid = (l + r) // 2
#               if nums[mid] > nums[r]:  # CHANGE 2
#                   l = mid + 1          # min strictly right
#               else:
#                   r = mid              # CHANGE 3: keep mid coz that mid can be the lowest agar mid-1 kela tar tey lose hou shakta
#           return nums[l]               # l == r is the answer
# ithe l<=r kela tar infinite loop hou shakta coz l=r is breaking while condn tech agar = dila tar infinite jain
# A binary-search loop must shrink the window every single iteration. If any branch can leave l and r unchanged, that branch + a non-terminating condition = infinite loop. like l=r

