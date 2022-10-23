import operator
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals=sorted(intervals,key=operator.itemgetter(0))
        n=len(intervals)
        i=0
        while(i<n):
            if(i+1==len(intervals)):
                break
            elif(intervals[i+1][0]<intervals[i][0] and intervals[i+1][0]==intervals[i+1][1]):
                i+=1
                continue
            elif(intervals[i][1]>=intervals[i+1][0]):
                x=intervals[i][0] if intervals[i][0]<intervals[i+1][0] else intervals[i+1][0]
                y=intervals[i][1] if intervals[i][1]>intervals[i+1][1] else intervals[i+1][1]
                intervals[i]=[x,y]
                intervals.remove([intervals[i+1][0],intervals[i+1][1]])
                n-=1
                i=-1
            i+=1
        return intervals
