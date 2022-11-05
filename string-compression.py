class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i=0
        j=0
        while(j<len(chars)):
            chars[i]=chars[j]
            counter=1
            while(j+1<len(chars) and chars[j]==chars[j+1]):
                j+=1
                counter+=1
            if(counter>1):
                for k in str(counter):
                    chars[i+1]=k
                    i+=1
            i+=1
            j+=1
        return i
