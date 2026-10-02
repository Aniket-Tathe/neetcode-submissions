# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

# A Binary Search Tree (BST) is a tree in which the values of all nodes in the left subtree of a node are less than the node's value, and the values of all nodes in the right subtree are greater than the node's value. Additionally, every subtree of a BST must also satisfy this property, meaning the "less than" or "greater than" condition is valid for all nodes in the tree, not just the root.

        # plist=[root]
        # qlist=[root]
        # p_val=[root]
        # q_val=[root]

        # if root<p: it should be root.val and p.val
        #     while root!=p:
        #         root=p_val.pop()

        #         if root.left:
        #             p_val.append(root.left)
        #             plist.append(root.left)
# You don't need a stack (p_val, pop). A stack is for when you might have to come back and try the other side. In a BST you never come back,
#      because the comparison tells you the one correct direction. So a single moving pointer is enough, like curr = curr.next in a linked list,
#      except you choose .left or .right each step.


        # if p or q is equal to root then root is the lca as thats the common before split
        # if (p or q) == root.val: hagla python will only check p == root.val
#         if p ==root.val or q == root.val:
#             return root
#         # use linkedlist traversal
#         p_travel=[root] # not root.val we need to return the treenode 
#         q_travel=[root]

#         curr=root 
#         while curr.val != p.val: # until we dont reach the value we traverse
#             print(curr.val)
#             if curr.val < p.val:
#                 curr=curr.right
#                 p_travel.append(curr) # not curr.val we need node    
#             else:
#                 curr=curr.left
#                 p_travel.append(curr)
        
#         curr2=root
#         while curr2.val != q.val: # until we dont reach the value we traverse
#             print(curr2.val)
#             if curr2.val < q.val:
#                 curr2=curr2.right
#                 q_travel.append(curr2) # not curr2.val we need node    
#             else:
#                 curr2=curr2.left
#                 q_travel.append(curr2)
#         # print(p_travel)
#         # print(q_travel)
    
#         # now to find common, sorting is not correct here it messes up the order
# #         At each node, the walk makes one choice: left or right. As long as p and q are on the same side, both walks make the same choice
# #   and reach the same node. The first time they make different choices, one goes into the left subtree and the other into the right.

# # so inshort the lca will be where the first split happens coz tyacha aadhi all common
#         lca=root # need node
#         for a,b in zip(p_travel,q_travel):
#             if a.val == b.val:
#                 lca=a # put either a or b its same, dont do a.val or b.val we need to return node
#             if a.val!=b.val:
#                 return lca

#         return lca

    ## neetcode soln: find the split 
        curr=root

        while curr: # this is a forever loop so we can keep iterating until we find split
            if p.val > curr.val and q.val > curr.val: # both > we go right
                curr=curr.right
            if p.val < curr.val and q.val < curr.val:
                curr=curr.left
            else: # found the split
                return curr