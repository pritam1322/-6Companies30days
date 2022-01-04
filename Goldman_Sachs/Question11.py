#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        """
        
        for idx in range(n):
            i = arr[idx] - 1
            while arr[idx] in range(1,n+1) and arr[idx] != arr[i]:
                arr[i],arr[idx] = arr[idx],arr[i]
                
        for i in range(n):
            if i+1 != arr[i]:
                return [arr[i],i+1]
        """
        
        rep = 0
        mis = 0
        for i in range(n):
            
            if arr[abs(arr[i])-1] < 0:
                rep = abs(arr[i])
            arr[abs(arr[i])-1] = -abs(arr[abs(arr[i])-1])
            
        for i in range(n):
            if arr[i] > 0:
                mis = i+1
                break
        return [rep,mis]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends