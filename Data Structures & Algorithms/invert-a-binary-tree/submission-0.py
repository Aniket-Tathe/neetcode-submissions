# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
# think binary tree like this:
# node, left,right and mag left node chya left right la None, similarly right node mag tyacha left,right is None
#  in recursion aadhi base case i.e kadhi baher paden hey decide karaicha mag khali recursion loop lihilay cha

        # if root is None:
            # return root # when root is empty i.e third case we give out either None or root both are valid
        
        # tmp,left=root.left,root.right hagla ithe
        # root.right=tmp
        # Trace [2,1,3]:
        # before:  2.left = 1, 2.right = 3
        # after:   2.left = 1, 2.right = 1     ❌ node 3 is gone and 1 appears twice
        # You need to assign to root.left and root.right directly. 
        # Use the a, b = b, a trick,    with root.left, root.right on the left side.

        # root.left,root.right=root.right,root.left

        # if root.left:
        #     return self.inverTree(root.left) # self is needed
        
        # if root.right:
        #     return self.inverTree(root.right) # self is needed


        # neetcode: DFS soln

        if root is None:
            return None
        
        # swap the children
        tmp=root.left
        root.left=root.right
        root.right=tmp

        self.invertTree(root.left) # left side invert kar
        self.invertTree(root.right) # right side invert kar

        return root
        
#       The question from before: does swap-before vs swap-after matter?

#   No. Both work:
#   - Swap then recurse (yours, called preorder): the children get swapped first, then each is inverted. Both still get visited.
#   - Recurse then swap (postorder): both subtrees get inverted first, then swapped. Same result.
# preorder, inorder, postorder bagh jupyter madhe with example
# pre is aadhi work,mag children
# inorder is left and right chya madhe work
# postorder is aadhi children mag work
