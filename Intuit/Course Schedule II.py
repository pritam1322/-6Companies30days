class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
