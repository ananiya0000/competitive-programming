class MyQueue(object):
    temp=[]
    def __init__(self):
        self.temp=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.temp.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if(self.empty()==False):
            x=self.temp[0]
            self.temp.remove(self.temp[0])
            return x
        return
        

    def peek(self):
        """
        :rtype: int
        """
        if(self.empty()==False):
            return self.temp[0]
        return
        

    def empty(self):
        """
        :rtype: bool
        """
        return False if self.temp!=[] else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
