class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        n = len(heights)
        m = len(heights[0])
        
        pac =set()
        alt = set()
        
        
        def dfs(r,c,visit):
            
            visit.add((r,c))
            
            for dr,dc in (0,-1),(0,1),(-1,0),(1,0):
                if r+dr in range(n) and c+dc in range(m) and (r+dr,c+dc) not in visit and heights[r+dr][c+dc] >= heights[r][c]:
                    dfs(r+dr,c+dc,visit)
            
            
            
        for i in range(n):
            dfs(i,0,pac)
            dfs(i,m-1,alt)
            
        for i in range(m):
            dfs(0,i,pac)
            dfs(n-1,i,alt)
            
        
        return pac.intersection(alt)
