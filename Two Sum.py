import collections

from valid_palindrome import solution


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sort_num = sorted(nums)
        def sercher(left,right):
            while right<len(nums) and sort_num[left]+sort_num[right]<=target:
                if(sort_num[left]+sort_num[right]==target):
                    return sort_num[left],sort_num[right]
                right+=1
            return '',''

        for i in range(len(nums)-1):
            left,right=sercher(i,i+1)
            if left==right and left!='':
                index=[i for i,x in enumerate(nums) if x==left]
                return index
            elif left!='':
                return nums.index(left),nums.index(right)



Solution=Solution()
a=Solution.twoSum([3,2,3],6)
print(a)
