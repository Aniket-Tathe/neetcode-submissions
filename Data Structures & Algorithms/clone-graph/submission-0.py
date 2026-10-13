# The grid in #200 was a graph without Node objects
# connected unidirected graph - An undirected graph is connected if there is a path between every pair of vertices
# • Connected Graph: Every vertex can reach every other vertex through a sequence of edges.
# • Disconnected Graph: The graph splits into two or more separate parts with no path between them.
# see explanations and 4 combinations of graph 
# connected, disconnected, undirected,directed jupyter has examples
#  # 200 no.of islands was undirected + disconnected and u use dfs for such. see jupyter

# neetcode soln:
# chupchap video bagh imp info aahe tyat, what type of clone we want
# copy is copy paste. if u change anything in copy, the other copy changes too.
# clone is like separate replica u make but values are of that copy. there is a diff. if u make changes to clone the original copy isnt changed 
# assignment vs shallow copy vs deep copy (clone) see diff in jupyter, here we want deep copy

# pretty much like every graph prob we use a hashmap
# undirected is 1-2 then 1 is neighbour of 2, and 2 is neighbour of 1, if 1 -> 2 this is direct 2 is neighbout of one but one isnt

# time comp is O(E+V) where E is edges and V is vertices

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew={}

        if node is None:
            return None

        def dfs(node):
            # if node not in deep_copy:
            #     deep_copy[node]=Node(val)
            
            # if node in deep_copy:
            #     return deep_copy[node]

            # if node.neighbours:
            #     for neighbour in neighbours:
            #         dfs(neighbour)
            if node in oldToNew: # if clone exists just return that clone
                return oldToNew[node]
            
            copy=Node(node.val) # if not then we add it
            oldToNew[node]=copy # old node to new node
            # this is the main code right adding node keep it oustide if: i mean u did if not then add. keep ifs for edge case and common case normal made lihi. which is repetitive

            # now node is added now we add its neighbours

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei)) # add the neighbours
            # once all the neighbours are done we return the copy

            return copy 
        
        return dfs(node)
# we can also do this with bfs
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        copy = {node:Node(node.val)} # new way of adding bagh 
        queue = deque([node])
        while queue:
            current = queue.popleft()
            for nei in current.neighbors:
                if nei not in copy:
                    queue.append(nei)
                    copy[nei] = Node(nei.val)
                copy[current].neighbors.append(copy[nei])
        return copy[node]