import math
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        output=[[0,0]]*k
        distances=[0]*k
        for i in range(len(points)):
            distance=(points[i][0]**2)+(points[i][1]**2)
            if(i<k):
                distances[i]=distance
                output[i]=points[i]
            else:
                maximum=distances.index(max(distances))
                if(distances[maximum]>distance):
                    distances[maximum]=distance
                    output[maximum]=points[i]
        return output
