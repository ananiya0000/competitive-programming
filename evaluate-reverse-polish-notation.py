class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                y,x=stack.pop(),stack.pop()
                if(i=="+"):
                    stack.append(int(x+y))
                if(i=="-"):
                    stack.append(int(x-y))
                if(i=="*"):
                    stack.append(int(x*y))
                if(i=="/"):
                    stack.append(int(float(x)/y))
        return stack[0]
