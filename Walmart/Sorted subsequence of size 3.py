#User function Template for python3


import heapq
class Solution:
    def find3number(self,arr, n):
        # code here
        
        
        mx = n-1 
        mn = 0
        
        sm = [0] *10000
        sm[0] = -1
        
        for i in range(1,n):
            if arr[i] <= arr[mn] :
                mn = i
                sm[i] = -1
                    
            else:
                sm[i] = mn
                    
                    
        lr = [0] * 10000
        lr[n-1] = -1
        
        for i in range(n-2,-1,-1):
            if arr[i] >=  arr[mx] :
                mx = i
                lr[i] = -1
                    
            else:
                lr[i] = mx
                
        for i in range(n):
            
            if sm[i] != -1 and lr[i] != -1:
                
                return [arr[sm[i]],arr[i],arr[lr[i]]]
                    
        return []
                    
                    
                    
                
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(100000)

def isSubSeq(arr, lis, n, m):
    if m==0:
        return True
    if n==0:
        return False
    if arr[n-1]==lis[m-1]:
        return isSubSeq(arr, lis, n-1, m-1)
    return isSubSeq(arr, lis, n-1, m)

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().strip().split()))
    lis = Solution().find3number(arr, n)
    # print(lis)
    # print(isSubSeq(arr, lis, n, len(lis)))
    if len(lis)!=0 and len(lis)!=3:
        print(-1)
        continue
    if len(lis)==0:
        print(0)
    elif lis[0]<lis[1] and lis[1]<lis[2] and isSubSeq(arr, lis, n, len(lis)):
        print(1)
    else:
        print(-1)
        
# } Driver Code Ends
