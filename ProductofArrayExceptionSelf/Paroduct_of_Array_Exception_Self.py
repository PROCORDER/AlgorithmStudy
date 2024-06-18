class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]

        leftproduct=[]
        product1=1
        for i in range(0,len(nums)):
            leftproduct.append(product1)
            product1*=nums[i]
        rightproduct=[]
        product2=1
        for i in range(len(nums)-1,-1,-1):
            leftproduct[i]*=product2
            product2 *= nums[i]
        return leftproduct
