# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # if not p or q: problem this will do if (not p) or q and not if (not p or q)
            # return False
        
        #case 1: both are empty return true
        if p is None and q is None:
            return True 
        # or u can do :
        # if not p and not q:
        #     return Ture
        
        if p is None or q is None: # case 2 either one is none
            return False 
        
        if p.val != q.val: # case 3 val is not equal
            return False
        
        # recurse for true, below hagla  == checks "are the two answers equal," not "are both True"
        # if self.isSameTree(p.left,q.left) == self.isSameTree(p.right,q.right):
            # return True

        if self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right): # checks condition both true or not
            return True
        else:
            return False
        
        # or
        # return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
           
        