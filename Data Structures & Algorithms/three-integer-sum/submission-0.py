class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # extension of 2sum
        # i+j+k=0 i.e i=-(j+k)
        
        # neetcode soln:
        res=[]
        nums.sort()

        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue  # i.e agar same value aahe i,i-1 then we skip 

            l,r=i+1,len(nums)-1
            while l<r:
                threesum=a+nums[l]+nums[r]
                if threesum<0:
                    l+=1
                elif threesum>0:
                    r-=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1 #ekach pointer update kartoy coz r automatically update hoin above
                    # condition mulw

                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res

# try the for loop mag 2sum hashmap kadhitari



            
        