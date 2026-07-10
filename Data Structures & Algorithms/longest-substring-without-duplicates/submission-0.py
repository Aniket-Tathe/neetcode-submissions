class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # jevha pan duplicate remvoal disen dokyat set() vaparta yein ka consider kar
        # abca "a disla" left varun "a" remove coz set() no duplicates allowed now set becomes 'bca'
        # if "cba" mag "b" aala then substring should be contiguos so first we remove c mag b 
        # why remove from left only and not middle? coz we want to keep it contiguous if u pop in middle continuous nahi rahnar
        # hence to remove "b" from cbab we needed to remove first c then b as no duplicates allowed and also need to be contiguous

        charset=set()
        l=0
        longest=0 # need to keep track of longest coz window is expanding and shrinking based on contiguous and duplicate condition

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            print(len(charset))
            longest=max(longest, len(charset))

        return longest


