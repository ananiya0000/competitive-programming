class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        dic={}
        dic[-1]=1
        output=[]
        for i in range(len(arr)):
            dic[i]=dic[i-1]^arr[i]
        for j in queries:
            x=j[0]
            y=j[1]
            output.append(dic[y]^dic[x-1])
        return output
