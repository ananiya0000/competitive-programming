class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        changed.sort()
        Q=deque([])
        output=[]
        for i in changed:
            if Q and Q[0]*2==i:
                output.append(Q.popleft())
            else:
                Q.append(i)
        return output if not Q else []
        
