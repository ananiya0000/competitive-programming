class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        output=[]
        while(i<len(nums)):
            if(i==0 or nums[i]>=nums[i-1]):
                i+=1
            else:
                temp=nums[i]
                nums[i]=nums[i-1]
                nums[i-1]=temp
                i-=1
        i=0
        while(i<len(nums)):
            if(nums[i]==target):
                output.append(i)
            i+=1
        return output
