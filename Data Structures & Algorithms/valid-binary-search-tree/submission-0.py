# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # if root and root.left:
        #     if root.val <= root.left.val:
        #         return False
        
        # if root and root.right:
        #     if root.val >= root.right.val:
        #         return False
        
        # # while root: 
        #     # return self.isValidBST(root.left) # direct return kela ki direct baher padtay
        #     # self.isValidBST(root.left) 
        # # while root:
        #     # self.isValidBST(root.right) 
        # # due to while this becomes an infinite loop , we dont need loop for recursion we just do
        # self.isValidBST(root.left)
        # self.isValidBST(root.right)
        
        # return True
        # above is still wrong as it will always give True , need to do something like
        # return self.isValidBST(root.left) and self.isValidBST(root.right) so it handles both true and false. var khup mistake aahe neet bagh kuthe haglay, learn to handle true false as condition in return statement instead of using separate while loop and if condn like above

# neetcode soln: 
# one is inorder traversal, inorder traversal for BST gives an increasing sorted array so if it doesnt follow that you return false and if follows then true
# rem in BST "all" the node in left of node including future children of the upcoming nodes 'all' should be small than node and "ALL" on the right side of node should be greater than parent node including the upcoming children. not even equal it should be less or more

# brute force is check parent root val is less than all values in left then check all val on the right and asa sagla value for each again compare all left and right, O(n^2)

# recursive DFS
# use the range -inf,inf, we use helper function
        def valid(node,left,right): # here left and right are the boundaries
            if not node:
                return True # becuase an empty BST is an BST
            
            if not (node.val < right and node.val > left):
                return False # as it broke our rule left<node<right
            
            # recursive call
            return (valid(node.left,left,node.val) # eg -inf < 1 < 2 inshort for left side, so parent is set to right boundary
            and valid(node.right,node.val,right)) # eg 2<3<inf 

        return valid(root,float("-inf"),float("inf")) # just use the helper function 
# hyacha video bagh coz agar mothi tree asen tar kasa asen and why we need range is imp