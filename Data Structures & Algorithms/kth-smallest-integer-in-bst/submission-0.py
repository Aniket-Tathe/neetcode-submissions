# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

# for sort, inorder when u use on BST u get a sorted list and then just index k will give ans

#         arr=[]
# # need a helper funcn coz varcha array la recursive gela tar every time arr intialize hoin:
#         def sor(root): # this we recurse
#             if not root:
#                 return None
            
#             # print(root.val)    ← here:   PREorder   (me first, then left, then right)
#             sor(root.left)
#             # print(root.val)    ← here:   INorder    (left, me, right)
#             arr.append(root.val)
#             sor(root.right)
#             # print(root.val)      # ← here: POSTorder  (left, right, me last)
#             # if u try inorder on a BST you will see it gives sorted 

#         sor(root)
#         # print(arr)  gives sorted array so kth smallest is just kth index

#         # return arr[k] # k starts from one while array from zero so we shift by one
#         return arr[k-1]
#         # can do better as we need just first k elements so instead of traversing whole we can stop at k
        
# method 2 is stop at k itself:
        # arr=[]
        # count=0 
        # def sor(root): # local funcn doesnt need self
        #     nonlocal count # so that sor can access count otherwise error in sor as it cannot access count
        #     if not root:
        #         return None
            
        #     if count>=k: # if we already have k just return
        #         return 
            
        #     sor(root.left)

        #     if count>=k: # left side found it
        #         return 

        #     arr.append(root.val)  # ← inorder spot: add me
        #     count+=1 # add the count

        #     sor(root.right)

        # sor(root)

        # return arr[k-1]

# neetcode soln:
# using iterative not recursive approach using stack coz when we add root later parat we need those so stack madhe ti value khali jain so we can access it later again
# visiting using stack also is inorder so u still get sorted list

        n=0
        stack=[]
        curr=root

        while curr or stack: # rem its or not and otherwise if one is None at end of left it will come out of loop
            while curr: # we go all left, add all left till None
                stack.append(curr)
                curr=curr.left # linkedlist traversal 
            
            curr=stack.pop() # pop recently value i.e at top
            n+=1

            if n==k:
                return curr.val
            
            curr=curr.right # go right when left side bcomes empty then all left again and so on,
