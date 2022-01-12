class Solution:

    #Function to find unit area of the largest region of 1s.
    def findMaxArea(self, grid):
        #Code here
        n = len(grid)
        m = len(grid[0])
        visit = set()
        area = 0
        
        
        
        def dfs(r,c):
            nonlocal count 
            count += 1
            visit.add((r,c))
            
            for dr,dc in (-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1):
                if r+dr in range(n) and c+dc in range(m) and grid[r+dr][c+dc] == 1 and (r+dr,c+dc) not in visit:
                    dfs(r+dr,c+dc)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i,j) not in visit:
                    count = 0
                    dfs(i,j)
                    area = max(area, count)
        return area
#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.findMaxArea(grid)
        print(ans)

# } Driver Code Ends
