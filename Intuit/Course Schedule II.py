class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
       """
       Kahn's Algo
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        ans = []
        
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]
        
        
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
            
        q = []
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        
        while q:
            node = q.pop(0)
            
            ans.append(node)
            
            for nei in graph[node]:
                indegree[nei] -= 1
                
                if indegree[nei] == 0 :
                    q.append(nei)
                    
        return ans if len(ans) == numCourses else []
    """
        
        
        
        graph = [[] for _ in range(numCourses)]
        
        for u,v in prerequisites:
            graph[v].append(u)
            
        def dfs(node):
            visit[node] = True
            rec[node] = True
            
            
            
            for nei in graph[node]:
                if visit[nei] == False:
                    if dfs(nei) == True:
                        return True
                elif rec[nei] == True:
                    return True
            
            ans.append(node)
            rec[node] = False
            return False
        
        
        visit = [False] * numCourses
        rec = [False] * numCourses
        ans = []
        
        for i in range(numCourses):
            if visit[i] == False:
                if dfs(i) == True:
                    return []
        return ans[::-1]
