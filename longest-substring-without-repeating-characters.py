class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited={}
        i=0
        ouptut=0
        for j in range(len(s)):
            visited[s[j]]=visited.get(s[j],0)+1
            while visited[s[j]]>1:
                visited[s[i]]-=1
                i+=1
            ouptut=max(ouptut,1+j-i)
        return ouptut
