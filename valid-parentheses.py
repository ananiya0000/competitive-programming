class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        output=True
        temp=[]
        for i in s:
            if(len(temp)==0):
                temp.append(i)
            elif(i==")" and temp[0]=="("):
                del temp[0]
            elif(i=="]" and temp[0]=="["):
                del temp[0]
            elif(i=="}" and temp[0]=="{"):
                del temp[0]
            else:
                temp.insert(0,i)
        if(len(temp)!=0):
            output=False
        
        return output
