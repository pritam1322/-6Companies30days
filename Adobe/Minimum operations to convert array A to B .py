#User function Template for python3
from bisect import bisect_left 

"""
1- add elements from A which are in B to list.
2- find LIS of that list
   to find LIS to vector if ele is greater than vector's last ele add to vector
   else insert that ele to right position using while loop or bisect_left(inbuilt method)
   
3 - answer = N-lis+M-lis
"""

class Solution:
    def minInsAndDel(self, A, B, N, M):
        # code here 
        
        i = 0
        j = 0
        count = 0
        
        def LIS(arr):
            if len(arr) == 0:
                return 0
                
            res = [0]*(len(arr)+1)
            
            l = 1
            
            res[0] = arr[0]
            
            for i in range(1,len(arr)):
                if arr[i] > res[l-1]:
                    res[l] = arr[i]
                    l += 1
            else:
                res[bisect_left(res,arr[i],0,l-1)] = arr[i]
            
            return l
        
        ans = []
        
        for i in range(N):
            if A[i] in B:
                count += 1
                ans.append(A[i])
                
        l = LIS(ans)
        return abs(N-l) + abs(M-l)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M=map(int,input().split())
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.minInsAndDel(A,B,N,M))
# } Driver Code Ends
