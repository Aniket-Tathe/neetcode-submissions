# refer #79 and 212 insrtead of words we have zero or one, this is easier if u refer that one

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROW,COLS=len(grid),len(grid[0])
        visited=set()
        count=0

        def dfs(r,c):

            # always write exit conditions first:
            if (r<0 or c<0) or (r>=ROW or c>=COLS) or grid[r][c]=='0' or ((r,c) in visited):
                return False

            # now if not we are at 1:
            visited.add((r,c)) # we add that path
            dfs(r+1,c) # no need of res = ur not returning anything here 
            dfs(r-1,c) 
            dfs(r,c-1) 
            dfs(r,c+1) # go all four directions
            # visited.remove((r,c))  dont use this here this is opposite of what u want 
            # understand why .remove doesnt need to be here and why #79 and 212 need to be look in jupyter
# for combinations u do try come back explore there .remove but here we are following a route/path and we dont want to revisit so we keep a track

            # count+=1  wrong place u are not counting 1 whenever u find 1 u are counting once so keep this out of dfs loop otherwise everytime u find one u add one. we are finding path. not no.of 1s in the grid.

        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    count+=1
                    dfs(r,c)
        
        return count

# A quick way to decide in future problems
# for .remove
#   Ask: "after I finish exploring from this cell, could a different valid answer need to pass through it?"

#   - Yes (routes, combinations, word paths) → backtracking: add, explore, remove.
#   - No (flood fill, counting groups, "can I reach X") → plain DFS: add, explore, never remove. u just add here becuase once a path is marked it stays marked for that u need that visited path to store somewhere and check in next iteration and make sure we dont reiterate 

# here 
# ok so here if we do 0,0 and 0,1 both are 1 we mark as one and since we have them in visited forever when we start from 0,1 we see if its already in path or no if not only then start the loop
# so here its like if u visited it then mark it, mark it means save that visited path so we dont revisit in future

# rem
# In #79 and the combination problems, a position has to be available again for the next attempt. If you left it marked, you'd be saying "never
#   go here again", and a later route or combination that genuinely needs that cell or number would be wrongly blocked. So you remove it when the current attempt is over.

#   Here in #200 it's the reverse: "never go here again" is exactly what you want, because that cell's island has already been counted.

#   ┌────────────────┬────────────────────────────────┬────────────────────────────────────────┐
#   │                │          marked means          │           so after exploring           │
#   ├────────────────┼────────────────────────────────┼────────────────────────────────────────┤
#   │ #39, #79, #212 │ "in use by the attempt I'm on" │ remove, so the next attempt can use it │
#   ├────────────────┼────────────────────────────────┼────────────────────────────────────────┤
#   │ #200           │ "already counted"              │ keep, so it's never counted twice      │
#   └────────────────┴────────────────────────────────┴────────────────────────────────────────┘

## neetcode soln: video bagh changla aahe
# this is actually a breath first search. bfs is an iterative algorithm not recursive
# wrote for loop first and then bfs, see video chupchap

        if not grid:
            return 0

        rows,cols=len(grid),len(grid[0])
        visit=set()
        islands=0

        # lastly we write bfs, iterative and bfs we use queue
        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c)) # set made append we do using .add not .append, .append is for list
            q.append((r,c)) # dequeue is .popleft() O(1), list pop is O(n)

            while q: # while q, expand the island
                row,col=q.popleft() # we first pop
                # 4 directions  down is 1,0, up is -1,0 , right is 0,1 ,  left is -1,0 
                directions=[[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    # check if its inbound
                    r,c=row+dr,col+dc
                    # our 4 conditions 
                    if r in range(rows) and c in range(cols) and grid[r][c]=='1' and (r,c) not in visit:
                        visit.add((r,c))
                        q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] =='1' and (r,c) not in visit: # rem no repeat position
                    bfs(r,c) # bfs is not a recursive algo its iterative
                    islands+=1 
        
        return islands

# Recursion is a stack: the most recent call is the one that runs, and when it returns you're back in the one before it. So recursion gives you
#   DFS order for free, with no data structure to manage.

#   There is no built-in mechanism that works like a queue, so for BFS you make one yourself (deque) and drive it with while q:. You did this in
#   #102 Level Order Traversal.

# ┌─────┬────────────────────┬───────────────────────────────────────────┐
#   │     │     recursive      │                 iterative                 │
#   ├─────┼────────────────────┼───────────────────────────────────────────┤
#   │ DFS │ yes, the usual way │ yes, with a list used as a stack (.pop()) │
#   ├─────┼────────────────────┼───────────────────────────────────────────┤
#   │ BFS │ not naturally      │ yes, with a deque (.popleft())            │
#   └─────┴────────────────────┴───────────────────────────────────────────┘