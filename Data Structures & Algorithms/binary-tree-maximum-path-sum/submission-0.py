# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
# postorder aahe we need children value before parent so its like left right me and at each me i.e parent we save that sum and build the tree bottom up

        res=float("-inf") # coz if we kept 0,then for -3 madhe compare will be 0,-3 mag scene 

        def postorder(root):
            nonlocal res
            if not root:
                return 0 # we are finding sum so None doesnt make sense 
            
            # postorder

            # if root.left: # no need for if statement as if not then ie will return 0 due to above condn
            #     postorder(root.left)
            # if root.right:
            #     postorder(root.right)
            
            # if root.val > res:
            #     res+=root.val

            # we need childrens value and also a value hence need a 'return'
            # we do traversal and addn in one go like the maxDepth problem
            left_value=max(0,postorder(root.left)) # if 0 left val is 0 and if neg then also 0
            right_value=max(0,postorder(root.right))

            maxval=root.val + left_value + right_value # this is current plus children

            res= max(res,maxval) # need to build path, # save: best path with me as top
            return root.val + max(left_value,right_value) # i.e my value + my better arm.
# we are doing two things, res is keeping best till yet, and return is doing my value + my better arm. this is same as 1 + maxDepth(left,right) fakt ithe root.val aahe coz it has val.         
        postorder(root)

        return res