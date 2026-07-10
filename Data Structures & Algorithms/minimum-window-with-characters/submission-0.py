class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # first grow till until you have all characters you need then shrink window as much as u can

        # hashmap={} # put all char we need here
        # for c in t:
        #     # if c not in hashmap:  this if would create issue for eg: t =AABC it will do just A,B,C we need duplicates also hence dropped if
        #     hashmap[c]=hashmap.get(c,0) + 1
        
        # print(hashmap)

        # l=0
        # minsub=0

        # for r in range(0,len(s)):
        #     while all(s[r] in hashmap):
        #         r+=1

        # got the logic half right but couldnt code

        # neetcode soln:
        
        if t=="":
            return ""

        countT, window={},{}

        for c in t:
            countT[c]=1+countT.get(c,0)
        
        have,need=0,len(countT)

        res,resLen=[-1,-1], float("inf") # [l,r] default u kept -1,-1 ani resLen we want min so default kept high
        l=0
        
        for r in range(len(s)):
            c=s[r]
            window[c]=window.get(c,0)+1 # update the window hashmap
            # now we check do we have the have=need condition

            if c in countT and window[c]==countT[c]:
                have+=1
            
            while have==need: # update the result
                if (r-l+1) < resLen:
                    res=[l,r]
                    resLen=(r-l+1)
                
                # now we try to shrink it from left to find min and which also satisfies have=need
                window[s[l]]-=1   # hashmap madhe value kami kartoy

                # aata while shrinking there comes a point where have != need:
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1  # means char kami zhalay have!=need then we decrement have
                l+=1

        l,r = res # after loop is over we take whats the l,r pointer to find the window

        return s[l:r+1] if resLen != float("inf") else "" # agar reslen inf nahiye ani improve zhaliye tar tyacha l,r+1 i.e window return kar
        # l:r+1, +1 karan python if [l,r] then l to r-1 jaato r exclusive hence +1
        # ani agar bhetla nahi kahi tar "" return kar

