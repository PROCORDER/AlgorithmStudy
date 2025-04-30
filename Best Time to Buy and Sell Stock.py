class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min=prices[0]
        max=prices[0]
        differ=0

        for i in range(1,len(prices)):
            if prices[i]<min:
                min=prices[i]
                max=prices[i]
            if prices[i]>max:
                max=prices[i]
            if differ<max-min:
                differ=max-min
        print(differ)
        return differ
Solution=Solution()
Solution.maxProfit(
[7,1,5,3,6,4]
)
