class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxprofit=0
        mn=prices[0]
        n=len(prices)
        for i in range(1,n):
            if prices[i]<mn:
                mn=prices[i]
            mxprofit=max(mxprofit,prices[i]-mn)
        return mxprofit