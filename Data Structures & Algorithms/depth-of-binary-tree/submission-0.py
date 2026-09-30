# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
# neetcode soln : 3 ways
    # DFS , DFS iterative i.e DFS without recursion, BFS 

# always first think of base case i.e lets say empty tree what would u return for max depth? 0

        # if root is None:
            # return 0
        
# we return the 1 + max(left,right) , 1 coz root is 1 so total is root plus whatver max is left or right side both O(n)

        # return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
# method 2: without recursion a) DFS  O(n)
    # BFS using a queue , see video

        # if not root:
        #     return 0
        
        # # deque if double ended queue library which allows for fast insertions and deletions see geeksforgeek for example 

        # level=0
        # q=deque([root])
        # # iterate while queue is empty and also in end count the level

        # while q: # while queue list exist

        #     for i in range(len(q)) : # we iterate over it and pop and add children and add lvl
        #         node=q.popleft() # pop and then we add its children only if they are available
        #         if node.left: # i.e node is not null i.e children aahe , left child add
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     # its like we are crossing each lvl
        #     level+=1 
        
        # return level
# method 3 dfs iterative, using stack and preorder. preorder is easier than postorder
# stack imagine khalun var yetoy tya mule when u add to stack in neetcode eg: 3 nantr 20 mag 9 aala not 9 nantr 20 coz we want to keep left node at top of stack mhanun aadhi 20 aadhi kela jo 9 chya khali jain mag same pop from top of stack, add its children and increase level. 

        if not root:
            return 0
        
        stack = [[root,1]] # base case var handle keliye where depth 0, tya mule ithe 1
        res=0

        while stack:
            node,depth=stack.pop()

            if node: # imp condn otherwise if null aala tar tey sudha stack madhe aad hoin
                res=max(res,depth)
                stack.append([node.right,depth+1]) # push right then left for preorder. ithe farak nai padat if u do below line above and above below but to go left to right traversal i.e stack logic we append aadhi right mag left so left is on top mag pop left 
                stack.append([node.left,depth+1])

        return res
