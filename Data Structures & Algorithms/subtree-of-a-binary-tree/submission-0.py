# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if root is None or subRoot is None:
        #     return False

        # if root.val == subRoot.val:
        #     if self.isSubtree(root.left,subRoot.left) and self.isSubtree(root.right,subRoot.right): # dont use == coz we want to comp boolean == compares nums not like is True == True/false:
        #         return True 
        
        # return False

        # iterative BFS try kar:

        # pahile root la subroot lvl la aan
        # while root.val != subRoot.val:
        #     if root.left is Not None: # nahitr inf loop hoin
        #         self.isSubtree(root.left,subRoot.val) # left ja
        #         if root.val != subRoot.val:
        #             break
            
        #     self.isSubtree(root.right,subRoot.val) # right ja
        # above code check kar hagtay logic

        # aata donhi lvl aahe
    
    ##### neetcode soln ########
        # tree problem la aadhi bagh recursive soln aahe ka coz that will be easiest to imp
        # always for tree problems start with the null function

        # mixture of sametree prob

    #     if root is None:
    #         return False
        
    #     if subRoot is None: # tricky part coz main tree madhe end la None asta leaf node che childs
    #         return True 
        
    #     if self.sametree(root,subRoot): # agar sametree ney true dila means aahe subtree direct true return 
    #         return True 
    #         # aata first root ani subroot same nahiye tya mule first same lvl var yeicha
    #         # bc traverse sudha tree madhe recursion ney karava lagta 
    #     return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
    #         # coz left or right la subtree ashu shakta tya mule "OR" v.imp 
    
    # def sametree(self,root,subRoot):

    #     if not root and not subRoot:
    #         return True 

    #     if root and subRoot and root.val==subRoot.val:
    #         return self.sametree(root.left,subRoot.left) and self.sametree(root.right,subRoot.right)
    #         # check left right same aahe ka 

    #     return False

    # bfs soln, 2 queue ek queue ney lvl var yeicha dusrya queue ney compare karaicha
    
    # if both at same lvl , compare func
        def bfs_match(root,subRoot): # def chya aat def no self needed as its local func
            q=deque([(root,subRoot)]) # if u just do [root,subRoot] error: need tuple

            while q:
                root,subRoot=q.popleft()
                if root is None and subRoot is None:     # ← add this FIRST
                    continue
                if (root and subRoot and root.val != subRoot.val) or (root is None or subRoot is None):
                    return False

                if root and subRoot: 
                    q.append((root.left,subRoot.left)) # again tuple (())
                    q.append((root.right,subRoot.right)) 

            return True

        # if both diff lvl
        q = deque([root])

        while q:
            root = q.popleft()
            if root.val == subRoot.val:
                if bfs_match(root,subRoot):
                    return True
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)# note fakta left iterate kartoy coz jo paryant left not equal to right subroot cha root value 
        return False

# remember agar iterative BFS or dfs kartoy tyat recursion nahi use karu shakat
# either recursion use kar of bfs/ dfs
