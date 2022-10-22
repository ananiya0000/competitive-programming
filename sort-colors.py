class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        while(i<len(nums)):
            if(i==0 or nums[i]>=nums[i-1]):
                i+=1
            else:
                temp=nums[i]
                nums[i]=nums[i-1]
                nums[i-1]=temp
                i-=1
        return nums
