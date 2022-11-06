class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        prefix=0
        dic={0:1}
        for i in nums:
            prefix=prefix+i
            if prefix-k in dic:
                count+=dic[prefix-k]
            dic[prefix]=1 if prefix not in dic else dic[prefix]+1
        return count
