class Solution:
    def isValid(self, s: str) -> bool:
        # print(list(s)) # building stack if ( open append if ) close .pop if end empty then valid

        # res=[]
        # for i in range(0,len(s)):
        #     if s[i]=="(" or s[i]=="{" or s[i]=="[":
        #         res.append(s[i])
        #     else:
        #         res.pop()  # takes index, not value. pop() defualt top cha remove karto
        # if len(res)==0:
        #     return True
        # return False
        # # even though above runs but has two problems: 1) if empty input then fails 2) you pop without checking if its the top
        # the order is off here ([)] should give false but tuzha true deta varcha coz order sathi kai kela nahiye safeguard
    
        # hashmap
        stack=[]
        closetoopen={')': '(', '}': '{', ']' : '['}

        for c in s:
            if c in closetoopen:
                if stack and stack[-1]==closetoopen[c]: # stack[-1] gives u top of stack, so if top matches we pop
                    stack.pop()
                else:
                    return False # means stack is not empty so we return false direct
            else:
                stack.append(c)
        
        return True if not stack else False

