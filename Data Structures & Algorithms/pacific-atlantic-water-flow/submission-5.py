# very intuitive problem, see video, instead of going each we go from outisde to inside at each side and return the common 

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
# new set at each position to trace the path 
# if we do dfs then it will be brute force and with time complexity O(nxm)^2. we do this in O(nxm) and the way we do it is dfs but instead of naively going from each position we choose both row and upper row only, upper for pacific and lower for atlantic. and left for pacific and right for atlantic.

        rows,cols=len(heights),len(heights[0])
        pac,atl=set(),set() # maintain sets for visited 
# saying height decreases from inside to outside for water to flow , we can say to go from outside to inside the height should increase
# we are going outisde to inside

# first we wrote the for loop below then we write the dfs function
        def dfs(r,c,visit,prevheight):
            # means (r,c) was visited, rem we are going from the ocean to the cells from outside to inside, if we go out of bound we return,
            if ((r,c) in visit or r<0 or c<0 or r==rows or c==cols or heights[r][c] < prevheight):
                return  # we want to go from low to high so if we see reverse we return

            # if above not return means we are at a good position so we add
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c]) # look here we pass our curr height for next dfs which becomes the prevheight when it goes into that loop
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for c in range(cols): # cover top bottom rows
            dfs(0,c,pac,heights[0][c]) # first row r=0 fix, prevheight is heights[r][c] this is pacific ocean
            dfs(rows-1,c,atl,heights[rows-1][c]) # last row, prevheight, this is for atlantic ocean

        for r in range(rows): # cover left right vertical 
            dfs(r,0,pac,heights[r][0]) 
            dfs(r,cols-1,atl,heights[r][cols-1]) 
        # after this visit would have updated all pacific and atlantic visit

        # now we try to find location which are in the pacific and atlantic ocean 
        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res

## look at this too:
# very intuitive problem, see video, instead of going each we go from outisde to inside at each side and return the common 

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
# new set at each position to trace the path 
# if we do dfs then it will be brute force and with time complexity O(nxm)^2. we do this in O(nxm) and the way we do it is dfs but instead of naively going from each position we choose both row and upper row only, upper for pacific and lower for atlantic. and left for pacific and right for atlantic.

        rows,cols=len(heights),len(heights[0])
        pac,atl=set(),set() # maintain sets for visited 
# saying height decreases from inside to outside for water to flow , we can say to go from outside to inside the height should increase
# we are going outisde to inside

# first we wrote the for loop below then we write the dfs function
        def dfs(r,c,visit,prevheight):
            # means (r,c) was visited, rem we are going from the ocean to the cells from outside to inside, if we go out of bound we return,
            if ((r,c) in visit or r<0 or c<0 or r==rows or c==cols or heights[r][c] < prevheight):
                return  # we want to go from low to high so if we see reverse we return

            # if above not return means we are at a good position so we add
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c]) # look here we pass our curr height for next dfs which becomes the prevheight when it goes into that loop
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for c in range(cols): # cover top bottom rows
            dfs(0,c,pac,heights[0][c]) # first row r=0 fix, prevheight is heights[r][c] this is pacific ocean
            dfs(rows-1,c,atl,heights[rows-1][c]) # last row, prevheight, this is for atlantic ocean

        for r in range(rows): # cover left right vertical 
            dfs(r,0,pac,heights[r][0]) 
            dfs(r,cols-1,atl,heights[r][cols-1]) 
        # after this visit would have updated all pacific and atlantic visit

        # now we try to find location which are in the pacific and atlantic ocean 
        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res
