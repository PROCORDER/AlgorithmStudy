#Return the two-number index of the array that can be added to create the target.
# leetcode twosum
"""
nums=[2,7,11,15]
target=9
maxlen=len(nums)
for item in range(maxlen):
    if item+1<maxlen:
        for i in range(item + 1, maxlen):
            if nums[item]+nums[i]==target:
                print(f"[{item},{i}]")
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,v in enumerate(nums):
            if target-v in nums[i+1:]:
                return [nums.index(v),nums[i+1:].index(target-v)+(i+1)]