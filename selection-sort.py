#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        arr=arr[i:]
        return arr
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(0,len(arr)):   
            for j in range(i+1,len(arr)):
                if(arr[i]>arr[j]):
                    temp=arr[j]
                    arr[j]=arr[i]
                    arr[i]=temp
        return arr

