class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
        # maxprofit=0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         profit=prices[j]-prices[i]
        #         if profit>maxprofit:
        #             maxprofit=profit
        # return maxprofit

        # see the example in jupyter find the cheapest 

        # cheapest=float("inf") # start with v.high nos:

        # maxprofit=0

        # for n in prices:
        #     cheapest=min(cheapest,n) # cheapest update value
        #     profit=n-cheapest # profit if i sell today
        #     # print(cheapest,"cheapest")
        #     # print(profit,"profit")
        #     if profit> maxprofit:
        #         maxprofit=profit
        #     # print(maxprofit,"maxprofit")

        # return maxprofit

        # neetcode soln: two pointer and sliding window
        # rem buy low sell high
        # l=buy,r=sell  here 

        maxprofit=0
        l,r=0,1

        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l] # sell-buy=profit
                maxprofit=max(maxprofit,profit)
            else:
                l=r # see video. you can skip many redundant calc with this you want l to be lowest
            r+=1
        return maxprofit
