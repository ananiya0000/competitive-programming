class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        j=len(cardPoints)-k
        subarr=sum(cardPoints[:j])
        current=subarr
        for i in range(len(cardPoints)-j):
            current+=cardPoints[j+i]-cardPoints[i]
            subarr=min(subarr,current)
        return sum(cardPoints)-subarr
