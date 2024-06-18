class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice=10000
        maxprofit=0
        for price in prices:
            minprice=min(minprice,price)
            maxprofit=max(maxprofit,price-minprice)
        return maxprofit
Solution=Solution()
prices=[7,1,5,3,6,4]
mx= Solution.maxProfit(prices)

