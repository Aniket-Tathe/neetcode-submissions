# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # # use bfs and save at every go
        # output=[]

        # q=deque([root]) # add to right and pop from left i.e FIFO first in first out pop

        # while q:
        #     current=[]
        #     for i in range(len(q)): # each for is a new lvl
        #         if not root: # otherwise in the last iteration it does None.val append 
        #             return current    
        #         root=q.popleft()
        #         current.append(root.val)

        #         if root.left:
        #             q.append(root.left)
                
        #         if root.right:
        #             q.append(root.right)
        #     output.append(current)
                 
        # return output
# time comp is O (n/2) the biggest tree if gets added in queue i.e the whole tree still it will be n/2, because its "binary" tree and O(1/2 x n) is just O(n)

## neetcode soln
        q=collections.deque()
        q.append(root)

        res=[]

        while q:
            current=[]
            qlen=len(q)
            for i in range(qlen):
                node=q.popleft()

                if node: # to handle the null case as well we add append inside this and also if children are present 
                    current.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if current:
                res.append(current)
    
        return res