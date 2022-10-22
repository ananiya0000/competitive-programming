class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        
        for n in nums:
            count=0
            for i in nums:
                if(i<n):
                    count=count+1
            output.append(count)
        return output
