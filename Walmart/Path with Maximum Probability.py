class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        graph = [[] for _ in range(n)]
        
        for i ,(x,y) in enumerate(edges):
            graph[x].append((y,succProb[i]))
            graph[y].append((x,succProb[i]))
        
        dist = [0] * n
          
        
        dist[start] = 1
        
        q = []
        q.append((start,1))
        
        while q:
            node, prob = q.pop(0)
            
            for nei,nei_prob in graph[node]:
                
                if dist[nei] < prob * nei_prob:
                    dist[nei] = prob * nei_prob
                    q.append((nei,dist[nei]))
                    
        return dist[end] 
