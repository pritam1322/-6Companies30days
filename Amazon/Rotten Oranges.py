class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = []
        visit = set()
        m = len(grid)
        n = len(grid[0])
        
        
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r,c))  
                elif grid[r][c] == 1:
                    visit.add((r,c))
                    
        ans = 0           
        while q and visit:
            for _ in range(len(q)):
                r,c = q.pop(0)
                for dr,dc in (-1,0),(1,0),(0,-1),(0,1):
                    if (r+dr,c+dc) in visit:
                        q.append((r+dr,c+dc))
                        visit.remove((r+dr,c+dc))
        
            ans += 1  
            
        return -1 if visit else ans
