class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        count=0
        j=len(people)-1
        i=0
        while i<=j:
            count+=1
            if(people[i]+people[j]>limit):
                j-=1
            else:
                i+=1
                j-=1
        return count
