class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}

        output=[]
        for i in nums:
            if i in hashmap:
                hashmap[i]=hashmap.get(i,0)+1
            else:
                hashmap[i]=1  # every integer cha int as key ani freq as value
        # print(hashmap)

        # all_repeat=sorted(hashmap.values(),reverse=True) # sorted but ek shot agar
        # values sames asle tar like [2,2,1] aata hey 2,2 kontya key che? problem? mhanun
        # key,value donhi save kar ani sort
        
        pairs=list(hashmap.items())
        # print(pairs)

        freq=sorted(pairs,key=lambda x: x[1],reverse=True) # lambda cha meaning, x ghe ani x[1] de 
        # if u just do key=x it says x undefined u need function mhanun lambda
        # x[1] chya value chya hishobane sort kar coz freq is [1] position, reverse for descending
        # print(freq) # this gives u number ani tyachi freq aata tyacha topk kadh
        # print(freq[:k]) now to slice first element of this list

        return [p[0] for p in freq[:k]]

    # neetcode soln : 
    # bucket sort: video bagh: where index = counts, value = list of nos wrt to that index count
    # eg: 0,1,2,3 index ithe 2 means occured twice so if [3,8,9] occured twice they will go at
    # index 2 hence index =counts and values = lists of those counts
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)] # +1 coz 0 index 0 occurence kuthlach nasen 
        # atleast ek tari asen so first zeroth slot empty ch asen hence +1 to mitigate true length

        for n in nums:
            count[n]=count.get(n,0)+1 # agar nasen 
        for number,counts in count.items():
            freq[counts].append(number)
        # print(freq)
        # aata top k
        result=[]
        for i in range(len(freq)-1,0,-1): # going from end to start 
            for n in freq[i]:
                result.append(n)

                if len(result)==k:
                    return result
        