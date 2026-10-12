# video bagh
# . can replace any char. so .ab mean . can be any a-Z and length of . is 1 so one char fill
# b.. means b aahe ka ani ajun 2 .. i.e .. here can be filled by any a-Z aahe ka eg: bat,bar,bus all should return True coz 2 .. and those can be any a-z so 
# we use Trie (prefix tree) data strucutre
# trie: first root then 26 children as a-z is 26 char
# we can do like dfs then for . we go to any random child then start search if we find the rest we return true and go through all childs if we find anywhere we return true and if not false
# wherever we see . it can be any char so we iterate over all possible options at that lvl

# remember backtracking che chale loops like for ney nahi hot tula recursion ch vaprava lagen mag like dfs use karun etc
# this problem is very good as in search function you have iterative portion (when u dont have . i.e normal) and recursive portion (dfs i.e when u have .)

# neetcode soln

# intialize the trienode this u have to do, isnt present at problem
class TrieNode():
    def __init__(self):
        self.children={} # lookup is fast
        self.endofword=False # by defualt false if we see end we make it true for that node

class WordDictionary:

    def __init__(self):
        self.root=TrieNode() # empty root then we add children to it later
        

    def addWord(self, word: str) -> None:
        # same code here as the trie prefix tree

        cur=self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
        
            cur=cur.children[c] # go to that c which is available so we search next char in word in the next for loop

        cur.endofword=True # mark end of that word as true
        
    def search(self, word: str) -> bool:
        # this is the main trick this is what changed, only this func is diff from trie prefix tree problem last one due to handling of .

        def dfs(j,child):
            cur=child

            for i in range(j,len(word)): # tuzha normal search loop
                c=word[i] # we do range and with j coz nusta c in word la pudhche char every dfs madhe kasa janar na parat tey reset hoin like c in word at each dfs we want as we do deep the loop to move forward mhanun i in range j, len word coz j ney pudha chaloy apan as we update j in each dfs as we go down  

                if c=='.': # extra condition for . baki same look at else its same from last prob
                    for child in cur.children.values(): # . disla ki children che jevdhe pan aahe we do back track one by one in them using dfs 
                        if dfs(i+1,child): # i + 1 mule aplyala j lagtay i.e one more and we run from j,len coz nusta len(word) asen tar each dfs word la parat 0 pasun vachel ani answer WRONG yeil (not just slow) we want if b.ab then . disla ki ajun pudhe ab length jain not b.ab hence we do range(j,len(word)) so we keep moving forward.
# by doing i+1 we go next lvl as at i there is . so next lvl we have 26 char options (max) direct .ab madhe u can to 'a' you need to fill it with one of this children value so we do i+1 and check what char can be filled inplace of . then if .ab then we chose 'c' then we see ab aahe ka  
                            return True # kuthe pan word complete zhala return True 
                    return False # ek pan nahi bhetla return false
                else:
                    if c not in cur.children: # normal search, this is iterative part 
                        return False
                    cur=cur.children[c]
            return cur.endofword # we see if its the endofword of not

        return dfs(0,self.root)


        
