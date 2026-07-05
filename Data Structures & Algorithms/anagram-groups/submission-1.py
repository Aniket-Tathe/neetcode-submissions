class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     hashmap={}
    #     for string in strs: # ithe keys is your anagrams ani value is your word
    #         # hashmap.setdefault(key, []).append(string)   # make [] if missing, then append
    #         # or
    #         # hashmap[key] = hashmap.get(key, []) + [string]
    #         hashmap["".join(sorted(string))]=hashmap.get("".join(sorted(string)),[]) + [string]
    #         # nahitr tuple kr dict key should be immutable means non changes
    #         # list is mutuable u can change hence hashamp[tuple(sorted(string))] not list
    #     # print(hashmap.values())
    #     return list(hashmap.values()) # comp (mxnXlogn) sorting logn gheta

    # remember append karaila .append cha syntax bagh agar normal hashmap[key]= xyz kaypan karshin
    # tar value overwrite hoin tya key madhli coz tu = kartoy either var cha syntax vapar or 
    # khalcha .append() to store multiple values in value for same key
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # comp (mxnx26)
        hashmap=defaultdict(list) # 

        for s in strs:
            count=[0]*26 # neetcode soln: a-z count kar 
            for j in s:
                count[ord(j)-ord("a")] +=1 # ASCHII char for eg: 
                # if a=74 then if j is a then 74-74=0, b=75 then 75-74=1 and so on upto 26
            hashmap[tuple(count)].append(s)
        print(hashmap) # hey bagh a-z cha tuple is tuzha key ani value tuzha tey word aahe
        return list(hashmap.values())
    