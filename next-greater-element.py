class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output=[]
        for i in nums1:
            updated=False
            j=nums2.index(i)
            for k in range(j+1,len(nums2)):
                if(nums2[k]>i):
                    output.append(nums2[k])
                    updated=True
                    break
            if(updated!=True):
                output.append(-1)
        return output
