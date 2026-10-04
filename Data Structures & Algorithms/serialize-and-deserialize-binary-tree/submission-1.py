# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
# the problem where we do preorder plus inorder to build the tree from list works here just extra part is instead of given list we encode them to strings but the place where it breaks is the duplicate values 

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string=[]

        def encoder(root):
            # nonlocal string no need if we use [] as list is updated we dont need nonlocal
            if root is None:
                string.append("null") # += and return cannot be in one line so split it
                return 

            # preorder is val,left,right traverse
            # string += str(root.val) if it was string=""
            string.append(str(root.val))
            encoder(root.left)
            encoder(root.right)
        
        encoder(root)

        # print(string)
        return ",".join(string)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        data=data.split(",")
        i=0
        # print(type(data))
        # print(data)
        def decoder(data):
            nonlocal i
            if data[i] == "null":
                i+=1
                return None

            root=TreeNode(int(data[i]))
            i+=1

            root.left=decoder(data) # or even root.left=decoder() coz data list is universal
            root.right=decoder(data)

            return root # return the root
        
        return decoder(data) # call the func let it build and return the root

# neetcode soln its same as above so skipped above is DFS 
# but can be done even with BFS
