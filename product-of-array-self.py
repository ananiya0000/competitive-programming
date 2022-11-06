class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        prefix=[1]*len(nums)
        suffix=1
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
        for i in range(n-1,-1,-1):
            prefix[i]*=suffix
            suffix*=nums[i]
        return prefix
