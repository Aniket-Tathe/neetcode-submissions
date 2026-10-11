class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

# popular problem 
# maybe can be also used for our CTC decoding with few conditions 

# previous in combination sum prob was append → recurse → pop and this is mark the cell as used → recurse → unmark it both are try → explore → undo

# also found this online easy explanation:
# Backtracking is just DFS on tree except there's no pre-defined tree. You have to build your own tree by passing the states through parameters.
# For example, normally when you do pre-order traversal, you go root -> root.left -> root.right. In backtracking involving choosing a number, left tree will be choosing the number and right tree not choosing. So you go left first by adding the number to path, call dfs(root.left). Pop it out of path (un-choosing) then dfs(root.right).

# neetcode soln:
# no optimised way and backtracking is just the brute force way which we do
        ROWS,COLS=len(board),len(board[0])
        path=set() # so no revisiting the same position twice within our path.

        def dfs(r,c,i):
            # always first write out exit conditions and then edge case mag main logic
            if i == len(word):
                return True
            
            if (r<0 or c<0 # going out of bound 
            or r>=ROWS or c>=COLS # going out of bound on upper end
            or word[i] != board[r][c] # found the wrong char
            or (r,c) in path): # if that r,c path that position is already in our path this is not choosing same position twice in path
                return False

            # if both above didnt trigger return it means we found our char so now we add that path, update and recurse
            path.add((r,c)) # rem set takes only one arg hence u need to .add(()) not .add(r,c)
            # now we added the found char and we run on next char i.e +1 on adjacent char on all 4 char
            res=(dfs(r+1,c,i+1) or # i+1 coz now we looking for new char
                dfs(r-1,c,i+1) or 
                dfs(r,c+1,i+1) or
                dfs(r,c-1,i+1))
            path.remove((r,c)) # as we no longer be returning to that position
            # rem .remove((r,c)) not .remove(r,c) set takes only one arg

            # if there is any path res will be true we return true if not then res will be false
            return res

        # now we recursive through each position
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): # if anywhere we find the dfs worked we return True immedidately
                    return True
        
        # if we never found we return false
        return False
    
# time complexity n x m (dim of board) x dfs (4^len(word)) so n x m x 4^len(word)
# 4 as we do row -1 plus one, col -1 plus one 