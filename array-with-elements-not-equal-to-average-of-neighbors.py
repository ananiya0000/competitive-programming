class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        i=1
        while(i<len(nums)):
            nums[i],nums[i-1]=nums[i-1],nums[i]
            i+=2
        return nums
