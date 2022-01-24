class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        lands = collections.deque()
        mx = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 :
                    lands.append(((i,j),0))
        
        
        while lands:
            for i in range(len(lands)):
                (r,c),d = lands.popleft()
                
                mx = max(mx,d)
                
                for dr,dc in (-1,0),(1,0),(0,-1),(0,1):
                    if r+dr in range(n) and c+dc in range(n) and grid[r+dr][c+dc] == 0:
                        
                        grid[r+dr][c+dc] = d + 1
                        lands.append(((r+dr,c+dc),d+1))
                        
        return mx or -1      
