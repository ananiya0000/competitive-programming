class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        nums_int=[int(x) for x in nums]
        count=1
        while(count<=len(nums)):
            output=max(nums_int)
            if(count==k):
                return str(output)
                break
            nums_int.remove(output)
            count+=1
        return
