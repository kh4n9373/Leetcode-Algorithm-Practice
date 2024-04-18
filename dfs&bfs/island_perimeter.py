class Solution:
    def islandPerimeter(self, grid: int) -> int:
        # dfs
        # r,c = len(grid),len(grid[0])
        # def dfs(i,j,visited=set()):
        #     if i > r-1 or j > c-1 or i < 0 or j < 0 or grid[i][j] == 0:
        #         return 1
        #     elif (i,j) in visited:
        #         return 0

        #     visited.add((i,j))
        #     res = 0 
        #     res += dfs(i, j + 1)
        #     res += dfs(i - 1, j)
        #     res += dfs(i, j - 1)
        #     res += dfs(i + 1, j)
        #     return res
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             return dfs(i,j)

        # Better solution without dfs
        r, c, Perimeter = len(grid), len(grid[0]), 0

        for i in range(r):
            for j in range(c):
                Perimeter += 4*grid[i][j]
                if i > 0:   Perimeter -= grid[i][j]*grid[i-1][j]
                if i < r-1: Perimeter -= grid[i][j]*grid[i+1][j]
                if j > 0:   Perimeter -= grid[i][j]*grid[i][j-1]
                if j < c-1: Perimeter -= grid[i][j]*grid[i][j+1]
                    
        return Perimeter

