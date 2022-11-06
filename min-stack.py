class MinStack(object):

    def __init__(self):
        self.stack=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if(len(self.stack)==0):
            self.stack.append((val,val))
            return
        [topper,minm]=self.stack[-1]
        if(val<minm):
            self.stack.append((val,val))
        else:
            self.stack.append((val,minm))
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        [topper,_]=self.stack[-1]
        return topper

    def getMin(self):
        """
        :rtype: int
        """
        [_,minm]=self.stack[-1]
        return minm


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
