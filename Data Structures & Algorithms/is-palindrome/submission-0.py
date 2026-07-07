class Solution:
    def isPalindrome(self, s: str) -> bool:
        # check the ord:if list same ascending and descending then yes
        # lookout for special chars they should be omitted
        # lookout for A,a in ASCII they are diff hence lowercase
        # print(list(s.lower()))
        # print(ord("a"),ord("A"),ord("z"),ord("Z"))
        # palin=[]
        # for string in list(s.lower()):
        #     if 97<=ord(string)<=97+26:
        #         palin.append(ord(string))
        # print(palin)

        #using c.isalnum() tells is "is this a letter or digit?"
        palin=[]
        for c in list(s.lower()):
            if c.isalnum():
                palin.append(ord(c))
        # print(palin)
        if palin == palin[::-1]: # [::-1] reverse check karta
            return True
        return False # you can also append normal char asa nahiye ki tula ord ch pahije
    
    # #neetcode soln:
    # def isPalindrome(self, s: str) -> bool:
    #     newstr=""

    #     for c in s:
    #         if c.isalnum():
    #             newstr+=c
    #     return newstr == newstr[::-1]
# what if the interviewer said no use of alnum and no new memory you made a new "" so extra mem
# soln 2 neetcode o(1) time
#     def isPalindrome(self, s: str) -> bool:
# # using 2 pointer left and right: if special char omit.
#         l=0
#         r=len(s)-1 # coz u start from zero

#         while l<r:
#             while l<r and not self.alphanum(s[l]): # ithe self.alphanum pahije coz if only alphanum error dein coz scope vegla aahe
#                 l+=1
#             while r>l and not self.alphanum(s[r]):
#                 r-=1
#             if s[l].lower()!=s[r].lower(): # better than == coz ek pan false aala ki direct baher
#                 # imp coz sometimes equal chya aivaji unequal check is more easier and efficient
#                 return False
#             l,r =l+1,r-1

#         return True

    # def alphanum(self,c):
        # return (ord("A")<=ord(c)<=ord("Z") or ord("a")<=ord(c)<=ord("z") or ord("0")<=ord(c)<=ord("9"))


