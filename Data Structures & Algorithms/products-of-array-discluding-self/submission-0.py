class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force
        # product=[]
        # for i in range(0,len(nums)):
        #     j=0
        #     prod=1
        #     for j in range(0,len(nums)):
        #         if j!=i:
        #             prod=prod*nums[j]
        #            # print(prod)
        #     product.append(prod)
        # return product

# Left products (product of everything strictly to the left; nothing to the left = 1):
#   index:        0    1    2      3
#   prefix:       1    1   1*2   1*2*3
#               = 1    1    2      6

# Now you do the mirror image — the right products (product of everything strictly to the right; nothing to the right = 1), built right-to-left:
#   index:        0        1      2    3
#   suffix:     4*3*2     4*3     4    1
#               = ?        ?      ?    ?

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        suffix=[1]*len(nums)

        # for index i you want the product excluding nums[i], so you must record the running product before multiplying nums[i] in.
        p=1
        for i in range(0,len(nums)):
            prefix[i]=p # notice the lag aadhi save mag multiply that creates the one lag
            p=p*nums[i] # or p*=nums[i] same thing
        
        s=1
        for i in range(len(nums)-1,-1,-1): # exclusive aahe mhanun len(nums) to -1 mhanje tey zero parynat jain
            suffix[i]=s
            s=s*nums[i]
        
        result=[]
        for i in range(len(nums)):
            result.append(prefix[i]*suffix[i])
        return result
# above u still stored two array more memory prefix and suffix extra

# neetcode 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Pass 1: result[i] = product of everything to the LEFT of i (store before multiply)
        prefix = 1
        for i in range(n):
            result[i] = prefix          # left-product goes straight into result
            prefix = prefix * nums[i]

        # Pass 2: multiply in the product of everything to the RIGHT, using one running var
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] = result[i] * suffix   # result[i] already holds prefix[i]; fold suffix in
            suffix = suffix * nums[i]

        return result

