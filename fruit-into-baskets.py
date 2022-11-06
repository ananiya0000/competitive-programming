class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        count={}
        i=0
        for j,k in enumerate(fruits):
            count[k]=count.get(k,0)+1
            if(len(count)>2):
                count[fruits[i]]-=1
                if(count[fruits[i]]==0): 
                    del count[fruits[i]]
                i+=1
        return j-i+1
