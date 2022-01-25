class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        grid_topleft = [a[:n//2] for a in grid[:n//2]]
        grid_topright = [a[n//2:] for a in grid[:n//2]]
        grid_bottomleft = [a[:n//2] for a in grid[n//2:]]
        grid_bottomright = [a[n//2:] for a in grid[n//2:]]
        row_sums = [sum(a) for a in grid]
        total = sum(row_sums)
        root = Node()
        if n == 1 or total == n*n or total == 0:
            root.isLeaf = True
            root.val = grid[0][0]
            root.topLeft = None
            root.topRight = None
            root.bottomLeft = None
            root.bottomRight = None
        else:
            root.isLeaf = False
            root.val = grid[0][0]
            root.topLeft = self.construct(grid_topleft)
            root.topRight = self.construct(grid_topright)
            root.bottomLeft = self.construct(grid_bottomleft)
            root.bottomRight = self.construct(grid_bottomright)
        return root
