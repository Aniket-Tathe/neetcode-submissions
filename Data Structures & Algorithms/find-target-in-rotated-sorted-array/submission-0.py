class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # whenever asked logn soln remember binary search, also if its sorted then bigger hint to use binary search
        # binary search usually 3 pointer left right ani mid and left<=r always 
        # l=0
        # r=len(nums)-1

        # if target in nums:
        #     while l<r: # rem either l<r you do or l<=r but mag possibility u skip some mid so need to save it in some variable
        #         mid=(l+r)//2
        #         if nums[mid]==target:
        #             return mid   
        #         elif nums[mid]>target:
        #             l=mid+1
        #         else:
        #             r=mid
        #     return l # when l=r while loop chya baher ye
        # else: 
        #     return -1  
        # prob with above eg: 4,5,6,7,0,1,2 and mid=6 targ=0 above code gives 2 not 0 even though cases passed
        

        # neetcode soln: tough prob aahe video bagh for concept
        # here we use l<=r becuase what id we are given [5] just one nos i.e l=r ithe
        # here u arent going till end last prob we went till end ithe target disla ki end mhanun l<=r
        l,r=0,len(nums)-1

        while l<=r:
            mid=(l+r)//2

            if nums[mid]==target:
                return mid
            
            # left sorted portion
            if nums[l]<=nums[mid]: # eg: 3,4,5,6,7,0,1,2 target =0 mid=6 left=3 we need to go right
                # if target>nums[l]: # it will be in right portion
                #     l=mid+1
                # elif nums[l]<target:  # tar=5 , left=3, mid=6
                #     l=mid+1 # still look right  
                # above both say look right so we combine
                if target>nums[mid] or target<nums[l]:
                    l=mid+1
                else: # nums[l]<target<nums[mid] search left
                    r=mid-1 # coz var if mid=target we return direct var condition aahe hence mid-1 instead of mid
                
            #if in right sorted portion
            else:
                # if target<nums[mid]: # eg: 7,0,1,2,3,4 tar=0 mid=1 we crop right
                    # r=mid-1
                # elif target>nums[r]:  
                    # r=mid-1  
                # both above same condn so we merge
                if target<nums[mid] or target>nums[r]:
                    r=mid-1
                else:
                    # target > middle and < right value we update left
                    l=mid+1
        
        return -1


