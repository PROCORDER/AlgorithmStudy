class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        temperaturesLength=len(temperatures)
        stack=[]
        List=[0]*temperaturesLength
        for i, item in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<item:
                last=stack.pop()
                List[last]=i-last
            stack.append(i)
        return List
