
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        solution=[]
        num=1
        for i in range(len(nums)):
            solution.append(num)
            num=num*nums[i]

        num=1
        for i in range(len(nums)-1,-1,-1):
            solution[i]=solution[i]*num
            num=num*nums[i]

        return solution

