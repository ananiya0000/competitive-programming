class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        output=[]
        count=Counter(p)
        i=0
        for j,k in enumerate(s):
            count[k]-=1
            while count[k]<0:
                count[s[i]]+=1
                i+=1
            if j-i+1==len(p):
                output.append(i)
        return output
