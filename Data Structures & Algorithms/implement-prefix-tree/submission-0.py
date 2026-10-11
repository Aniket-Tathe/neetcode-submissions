# need TrieNode: this wasnt given in question so need to build yourself
class TrieNode:
    def __init__(self):
        self.children={} # hashmap
        self.endofword=False # by default false if we wanna mark some word end we do true 
    # why like this ?
    # we can do for eg: children["a"] = TrieNode() so for "a" we create 

# a trie is a tree in which every node uses a hashmap to hold its children.

#   - Binary tree node: two fixed slots, left and right.
#   - Trie node: a hashmap of slots, created only when needed and keyed by letter, plus the endofword flag.

class PrefixTree:
# auto complete and spell checker system
# trie is also known as prefixtree
# video bagh chupchap bhari aahe neetcode

# if we just want insert and search we can just hashmap and hashset whose O(1) for this startswith we need this tree structure to check prefix
# why? imagine list of 1million words and u need to see startswith 'b' the thing is in normal setting it will be very huge to see if any of those words startswith 'b' but there see video how the trie looks like, we need to just see is there any node here its first letter so check if any child has the letter 'b' and we are done. 
# first layer will be 26 char as a-Z so 26 child at max at first lvl
# to check will be O(1)

    def __init__(self):
        self.root=TrieNode() # just make the root, this will be empty tree
        
    def insert(self, word: str) -> None:
        # iterate over every char in the word
        cur =self.root # start at the root

        for c in word:
            # does this char already exists in our tree?
            if c not in cur.children: # if it doesnt exist in our hashmap we create it
                cur.children[c] = TrieNode() # we add that children
            # we use char c as a key value

            # now if it exists we just do:
            cur=cur.children[c] # move cur to that child c and for next iterations we keep building that respective child
            # its like hashmap inside hashmap see jupyter and examples to know its like hashmap tree, examples bagh chupchap nahitr nai samajnar
        
        # now we are at end of word so we make that endofword false as true
        cur.endofword=True

    def search(self, word: str) -> bool:
        cur=self.root

        for c in word:
            if c not in cur.children:  
                return False

            cur=cur.children[c]
        
        if cur.endofword: # once we traverse till end, in the end we check are we at end
            return True
        # if we search app this will have issue as app is in apple the prefix func is below one where it should return true if it has app prefix but this is search app in apple is not correct there should be separate app. its search. if apple is there but app not and u search app it should return false
# for apple this will return true as endofword will be true for app it will be false as even though it found app through apple the endofword at app end char p was still false
        return False
        
    def startsWith(self, prefix: str) -> bool:
        
        cur=self.root

        for c in prefix:
            if c not in cur.children:  
                return False

            cur=cur.children[c]
        
        # here we just skip endofword check coz we are not doing search, app in apple should return true
        return True 
# inserting is O(n), lookup is O(1) due to hashmap 