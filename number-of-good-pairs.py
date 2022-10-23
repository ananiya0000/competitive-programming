class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output=0
        i=0
        while(i<len(nums)):
            j=i
            while(j<len(nums)):
                if(nums[i]==nums[j] and i<j):
                    output+=1
                j+=1
            i+=1
        return output
