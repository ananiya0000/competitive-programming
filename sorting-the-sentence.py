class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss=s.split()
        arr=[""]*9
        final=""
        for i in ss:
            temp=int(i[-1])
            arr[temp-1]=i[:-1]
        for j in arr:
            if(j!=""):
                final=final+str(j)+" "
        final=final.strip()
        return final
