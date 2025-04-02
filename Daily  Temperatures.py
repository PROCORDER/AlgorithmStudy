class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack=[]
        answer=[0]*len(temperatures)
        for cur_index,temper in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temper:
                before_index=stack.pop()
                answer[before_index]=cur_index-before_index
            stack.append(cur_index)
        return answer



Solution=Solution()
Solution.dailyTemperatures([73,74,75,71,69,72,76,73])