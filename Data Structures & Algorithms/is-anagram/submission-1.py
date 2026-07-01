# class Solution: # build two hashmap and compare 
#     def isAnagram(self, s: str, t: str) -> bool:
#         hashmap1={}
#         hashmap2={}

#         if len(s)!=len(t):
#             return False
#         else:
#             for i in range(0,len(s)):
#                 if s[i] in hashmap1:
#                     hashmap1[s[i]]+=1
#                 else:
#                     hashmap1[s[i]]=1
#                 if t[i] in hashmap2:
#                     hashmap2[t[i]]+=1
#                 else:
#                     hashmap2[t[i]]=1
#             if hashmap1 == hashmap2:
#                 return True
#             else:
#                 return False

# build one hashmap increment when you find in one decrement when found in another in the end 
# if all zero then anagram if not then no:
# class Solution: # build two hashmap and compare 
#     def isAnagram(self, s: str, t: str) -> bool:
#         hashmap={}

#         if len(s)!=len(t):
#             return False
#         else:
#             for i in s:
#                 if i not in hashmap: # build hashmap first
#                     hashmap[i]=1
#                 else: 
#                     hashmap[i]+=1
#             for i in t:
#                 if i not in hashmap:
#                     hashmap[i]=-1 # if kept +1 if there is a char that is in t and not s it will get added as +1 but it should be -1
#                 else:
#                     hashmap[i]-=1
            
#             # all and any bagh: all means all satisfy, any means atleast ekane kela pahije satisfy
#             return all(v==0 for v in hashmap.values())

# same as above but using .get function 
class Solution: # build two hashmap and compare 
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap={}
        if len(s)!=len(t): # agar length ch same nasen mag anagaram nahi hou shakat tey tya mule aadhich check
            return False 
        else:    
            for i in s:
                hashmap[i]=hashmap.get(i,0)+1 # get i agar nasen tar 0 return kar, handles both if i not present add it, if present +1 increment
            for i in t:
                hashmap[i]=hashmap.get(i,0)-1 # get i agar nasen tar 0
            
            return all(v==0 for v in hashmap.values())

# built in functions 
# class Solution: # build two hashmap and compare 
    # def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
    # or can use sorting as after sorting fucntion
        # return sorted(s) == sorted(t)
