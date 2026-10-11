class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

# backtracking is try a choice, explore, undo it
# You build a combination one number at a time. At each step you make a choice, go deeper to see where it leads, then undo the choice and try the next one. It's DFS on a tree of decisions rather than on a tree of nodes.

# here we want 3,2,2 = 7 and 2,2,3 = 7 both are sum 7 but we dont want both to be added in results i.e we want combinations not permutations that sum upto 7 
# permutation: order does matter, eg: here [2, 2, 3], [2, 3, 2] count as diff unique, which the prob says is not unique if the total sum is same.
# combination: order does not matter, eg: [2, 2, 3], [2, 3, 2], and [3, 2, 2] are all the exact same combination because they all contain two 2s and one 3 
# so we want combination not permutation.

# watch neetcode soln
# root then take 2 left or not 2 right this way we separate duplicates down the lane
# so left is inlcude and right is not, this is main logic and imp for recursion
# time complexity 2^t where t=target, at each step we are making 2 decision hence 2^

        res=[]

        def dfs(i,curr,total):
            if total==target: # if target is reached we append that comb to res
                res.append(curr.copy()) # .copy() very important coz we need cur ahead to recurse so if we just append we cant use that combinations, we dont wanna modify cur
                return # coz we found target we stop recursing that branch
            
            if i>=len(nums) or total > target: # if we go out of bound with i 
                return # we just stop that branch

            curr.append(nums[i]) # we add the same number here this is include left branch
             # update total
            dfs(i,curr,total+nums[i]) # i stays same, so this is left branch we adding dupliactes
            # the right branch where we skip it, so we pop, since we did .append that val we need to pop that as right side is without so before we traverse right side we pop v.imp 
            curr.pop() # coz we appended on left side we pop on right to continue without that val
            # curr.append(nums[i+1]) this is wrong this will append additional we have recurive below so let that handle curr.append which we already do inside and below is i+1 
            dfs(i+1,curr,total) # here we moved i so this is right branch which is without, total stays same so we just pass total
        dfs(0,[],0) # i=0, cur=[] start root at empty then add left or no add right traverse, total=0
        return res 
            

####### below is permutation where each seq is unique i.e 3,3,2 and 2,3,3 is treated diff

def permutationSum(nums, target):
    res = []

    def backtrack(cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if total > target:
            return

        # At every step, check ALL numbers from the beginning
        for num in nums:
            cur.append(num)
            backtrack(cur, total + num)
            cur.pop() # Backtrack

    backtrack([], 0)
    return res

             
# • Permutation Complexity: The tree explodes in width. With an array of 5 elements, every single step attempts 5 loops. It finds 6 valid answers.
# • Combination Complexity: The tree is binary (only 2 choices per node: keep or skip). Because it can never look backward to an earlier element, it naturally filters out the clutter and finds only the 3 mathematically unique sets.

# permutation exmaple it grows wide as at each step u have all options available instead of combination where we do choose or no choose

# see below the visualization diff between permuatation vs comvbination tree

# permutation tree
#                            [ Sum = 0 ]
#          /           /          |          \           \
#      Pick 2       Pick 3     Pick 5     Pick 7       Pick 9
#       /            /            |          |            \
#  [Sum=2]       [Sum=3]      [Sum=5]    [Sum=7]🎉     [Sum=9]❌ (>7)
#   / | \ \ \     / | \ \ \    / | \ \ \
#  2  3 5 7 9    2  3 5 7 9   2  3 5 7 9
# ...            |            |
#             [Sum=5]      [Sum=7]🎉 ([5, 2])
#                |
#             [Sum=7]🎉 ([3, 2, 2])

# combination tree
#                                 [ Index 0: num = 2, Sum = 0 ]
#                                /                             \
#                        Keep 2                                 Skip 2
#                       /                                         \
#         [ Index 0: num = 2, Sum = 2 ]                 [ Index 1: num = 3, Sum = 0 ]
#                /             \                                /              \
#           Keep 2              Skip 2                      Keep 3              Skip 3
#             /                   \                          /                    \
#   [Index 0: Sum=4]        [Index 1: num=3, Sum=2]    [Index 1: Sum=3]     [Index 2: num=5, Sum=0]
#      /         \               /         \             /        \              /         \
#   Keep 2      Skip 2        Keep 3      Skip 3      Keep 3     Skip 3       Keep 5      Skip 5
#    /             \           /             \          /          \           /             \
# [Sum=6]     [Index 1:Sum=4] [Sum=5]     [Index 2:Sum=2] [Sum=6] [Index 2:Sum=3] [Sum=5]   [Index 3:Sum=0]
#                /        \                  /        \              /        \               |
#             Keep 3     ...              Keep 5     ...          Keep 5     ...             ...
#              /                           /                        /
#           [Sum=7]🎉([2,2,3])          [Sum=7]🎉([2,5])         [Sum=8]❌
