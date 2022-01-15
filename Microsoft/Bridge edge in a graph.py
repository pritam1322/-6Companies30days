#User function Template for python3

class Solution:
   
    #Function to find if the given edge is a bridge in graph.
    def isBridge(self, V, adj, c, d):
        # code here
        
        def dfs(c,d):
            if c == d:
                return True
                
            visit[c] == True
            
            for node in adj[c]:
                if visit[node] == False:
                    if dfs(node, d):
                        return True
                        
                        
            
            return False
            
        visit = [False] * V
        res = [0] * V
        for i in range(V):
            for val in adj[i]:
                if (i == c and val == d) or (i ==d and val == c):
                    continue
                
                res[i] = val
                
        bl = dfs(c,d)
        
        return (not bl)
        
        
        
        
        
        
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
            
        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i])) 
            
        c,d=map(int,input().split())
        ob = Solution()
        
        print(ob.isBridge(V, adj, c,d))
# } Driver Code Ends
