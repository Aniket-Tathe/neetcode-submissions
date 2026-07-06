class Solution: # see neetcode soln video

    def encode(self, strs: List[str]) -> str:
        # encoded_string=[]
        # for string in strs:
        #     encoded_string.append(str(len(string)))
        #     encoded_string.append('#')
        #     for char in string:
        #         encoded_string.append(char)
        # # print(encoded_string) # gives u list of string like [5, '#', 'H', 'e', 'l', 'l', 'o', 5, '#', 'W', 'o', 'r', 'l', 'd']
        # # aata ulta join to make it one str using "".join(list)
        # print("".join(encoded_string)) # gives 5#Hello5#World
        # return "".join(encoded_string) 
        #above was yours below is neetcode

        res=""

        for s in strs:
            res+=str(len(s))+"#"+s
        print(res)

        return res

    def decode(self, s: str) -> List[str]:

        res=[]
        i=0
        # two pointer ney length aadhi kadhaichi mag tey # to length j+1 iterate in s 
        # moving window aahe mhanun j+1:j+1+length karava lagen not j+1:length 
        # coz if j=8 ani length 5 mag tey 8:5 hoin that is not correct moving pahije
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            print(length)
            res.append(s[j+1:j+1+length]) 
            i = j+1+length 
        return res

        

