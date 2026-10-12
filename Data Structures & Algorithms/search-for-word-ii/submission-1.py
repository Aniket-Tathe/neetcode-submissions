# trie soln with dfs backtrack: backtrack is like append dfs then pop
class TrieNode():
    def __init__(self):
        self.children={}
        self.endofword=False

# brute for is just looped version of word search prob
#   result = []
#   for each word in words:
#       if exist(board, word):     # your #79 solution, unchanged
#           add word to result
# for each word if we do dfs for each word we need to check every posn
# time compl (m x n x 4 ^mxn ) x w where w=no.of words we check

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root=TrieNode()

        def addword(word):
            curr=root
            for c in word:
                if c not in curr.children:
                    curr.children[c]=TrieNode()
                
                curr=curr.children[c]
            curr.endofword=True
        
        for word in words:
            addword(word)
        
# traverse the trie
        res=set() # set coz there can be multiple same word in words
        path=set() # for saving visited paths

        ROW,COLS=len(board),len(board[0])
        def dfs(r,c,node,word): # row,col,char which we check, here word means word formed so far
            # condn where it will exit
            if (r<0 or c<0) or (r>=ROW or c>=COLS) or (board[r][c] not in node.children) or ((r,c) in path): # not (r,c in path)
                return False  # u can also jusr return . i.e None as None counts as False also
            # >= coz python start from 0. so == means out of bound for us as we run 0 to len -1 

            # if node.endofword: 
                # res.add(word) # if added here it will go till back but not backend 
            
            # now we traverse
            path.add((r,c)) # add the current path then we look left right above down
            # we move the node to next child
            node=node.children[board[r][c]]

            word = word + board[r][c]             # notepad grows by this cell's letter
            if node.endofword: 
                res.add(word) # not return res.add(word) coz return disla ki baher padta function, we add that letter and see if its end if yes then add to set.
# rem: move the node first, update the word, then check endofword, then add

            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            path.remove((r,c)) # backtrack


        for r in range(ROW):
            for c in range(COLS):
                dfs(r,c,root,"") # start empty and we fill as we go


        return list(res) # whatever we found we return


            
            
