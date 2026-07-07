class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # print(heights)

        l=0
        r=len(heights)-1
        # print(len(heights))
        maxarea=0

        while l<r:
            area=(r-l)*min(heights[l],heights[r]) # width * height
            print(area)
            if area>maxarea:
                maxarea=area
            if heights[l]>heights[r]: # jey chota aahe tey pointer move kar so that both pointer move
               # coz lets say height l=8 and r=2 then why would u just shift l when u have 8>2 hence shift 2
               # u missed this tu direct nusta left +1 karat hota but what if left height>right hence below
                r-=1
            else:
                l+=1
        return maxarea

# neetcode soln:
    # def maxArea(self, heights: List[int]) -> int:
    #     # first brute force loop all: O(n2)
    #     # maxarea=0
    #     # for i in range(0,len(heights)):
    #     #     for j in range(i+1,len(heights)):
    #     #         area= (j-i)*min(heights[j],heights[i])
    #     #         if maxarea<area:
    #     #             maxarea=area
    #     # return maxarea

    #     # optimal 2 pointer O(n)
    #             l, r = 0, len(heights) - 1
    #     res = 0

    #     while l < r:
    #         area = min(heights[l], heights[r]) * (r - l)
    #         res = max(res, area)
    #         if heights[l] <= heights[r]: # notice here u forgot = in above, did not consider if both height same
    #             l += 1
    #         else:
    #             r -= 1
    #     return res


