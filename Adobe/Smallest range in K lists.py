#User function Template for python3
import heapq
class Solution:
    def smallestRange(self, arr, n, k):
        # code here
        # print the smallest range in a new line
        q = []
        
        low = 0 
        high = 0
        mn = float('inf')
        mx = float('-inf')
        Range = float('inf')
        
        for i in range(k):
            heapq.heappush(q,(arr[i][0],(i,0)))
            mn = min(mn, arr[i][0])
            mx = max(mx, arr[i][0])
            
        while True:
            min1,(r,c) = heapq.heappop(q)
             
            if Range > mx - min1:
                 
                mn    = min1
                low   = mn
                high  = mx
                Range = mx-mn
                
            if c == n-1:
                break
            
            heapq.heappush(q, (arr[r][c+1], (r,c+1)))
            
            if mx < arr[r][c+1]:
                mx = arr[r][c+1]
                
        return low,high
      
      
#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    line=input().strip().split()
    n=int(line[0])
    k=int(line[1])
    numbers=[]
    for i in range(k):
        numbers.append([int(x) for x in input().strip().split()])
    r = Solution().smallestRange(numbers, n, k)
    print(r[0],r[1])
# } Driver Code Ends
