class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = [[] for _ in range(n+1)]
        
        for u in range(n):
            for v in range(n):
                if isConnected[u][v] == 1 and u != v:
                    graph[u+1].append(v+1)
                    
                    
        def dfs(node):
            visit.add(node)
            
            
            for nei in graph[node]:
                if nei not in visit:
                    dfs(nei)
            
        count = 0
        visit =set()
        for i in range(1,n+1):
            if i not in visit:
                dfs(i)
                count += 1
                
        return count  
