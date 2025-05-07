class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        dict={}
        count=0
        for stone in stones:
            if stone not in dict:
                dict[stone]=1
            else:
                dict[stone]+=1
        for jewel in jewels:
            if jewel in dict:
                count+=dict[jewel]
        return count