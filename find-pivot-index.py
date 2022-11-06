class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if(n==1):
            return 0
        prefix=nums[:]
        suffix=nums[:]
        for i in range(1,n):
            prefix[i]+=prefix[i-1]
        for j in range(n-2,-1,-1):
            suffix[j]+=suffix[j+1]
        if(suffix[1]==0):
            return 0
        for k in range(1,n-1):
            if(prefix[k-1]==suffix[k+1]):
                return k
        if(prefix[-2]==0):
            return n-1
        return -1
