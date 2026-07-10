class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # watch the neetcode soln:
        # O(26.n)
        # main idea: window - max count <=k if not then we dont have room for edit if yes then we increase window

        # count={}
        # l=0
        # maxcount=0

        # for r in range(len(s)):
        #     count[s[r]]=count.get(s[r],0)+1 # we are mapping char to counts : like A : 1 

        #     while (r-l+1) - max(count.values()) > k:
        #         l+=1 # if it gets out of max edits allowed we shift the window
            
        #     maxcount=max(maxcount,(r-l+1)) # if we are inside edits, the max substring becomes our window size

        # return maxcount
    
        # ii) O(n) soln using maxf
        count={}
        l=0
        maxf=0
        res=0

        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1 # we are mapping char to counts : like A : 1 

            maxf = max(maxf, count[s[r]])
            while (r-l+1) - max(count.values()) > k:
                count[s[l]]-=1
                l+=1 # if it gets out of max edits allowed we shift the window
            
            res=max(res,(r-l+1)) # if we are inside edits, the max substring becomes our window size

        return res