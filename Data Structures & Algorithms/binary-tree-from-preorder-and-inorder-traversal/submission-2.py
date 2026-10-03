# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
# # preorder is print,left,right mag inorder is left,print,right start preorder sangen mag next value inorder mag parat pre and so on
#         # root=TreeNode()

#         # while preorder or inorder: # we pop until there are no values to pop then while end
#         #     root.val=preorder.pop()
#         #     root.left=inorder.pop()
#         # # no need for while tbh but recursion needed ani recursion sathi while loop not needed
        
#         # return root

# # remember think of recursive as a while loop, if u have recursive no need for while 
# ### neetcode soln:
# # hard aahe, video bagh chupchap for understanding

#         if not preorder or not inorder: # base case for recursion
#         # when u just do if not preorder or inorder it is if (not preorder) or inorder: hence need the not on both ends
#             return None   
        
#         root=TreeNode(preorder[0]) # always first value
#         # now find the index of this value in the inorder array
#         mid=inorder.index(preorder[0]) # coz tya value chya left la jey asen tey left aahe
#         root.left=self.buildTree(preorder[1:mid+1],inorder[:mid]) # pass the new preorder and inorder arrays for next iter tya mule sliced array 1:mid+1 is just till mid as python is exclusive and we start from 1 as we used 0 in preorder[0], :mid upto mid but not mid
#         root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:]) # mid chya pudhcha consider kar
#         return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # value → its index in inorder, built once so every lookup is O(1) instead of .index() scanning
        pos = {v: i for i, v in enumerate(inorder)} # awesome way to build dictionary k,v becomes v,k
        pre_i = 0                      # pointer into preorder: the next root to build

        def helper(lo, hi):            # build the subtree that uses inorder[lo..hi]
            nonlocal pre_i             # we reassign pre_i (+= 1), so it needs nonlocal
            if lo > hi:                # empty range → no subtree
                return None

            root = TreeNode(preorder[pre_i])   # preorder gives roots in exactly the order we build them
            pre_i += 1

            mid = pos[root.val]                # where the root sits in inorder
            root.left = helper(lo, mid - 1)    # left part of the range (must come BEFORE right)
            root.right = helper(mid + 1, hi)   # right part of the range
            return root

        return helper(0, len(inorder) - 1)