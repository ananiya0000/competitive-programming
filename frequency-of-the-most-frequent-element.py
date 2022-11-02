class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i=0
        j=0
        while(i<len(nums)):
            k+=nums[i]
            if(k<(nums[i]*(i-j+1))):
                k-=nums[j]
                print("here")
                j+=1
            i+=1
        return i-j
