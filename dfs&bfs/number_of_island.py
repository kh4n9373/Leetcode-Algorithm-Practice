
def numIslands(grid: str) -> int:
    r,c = len(grid), len(grid[0])
    res = 0 
    visited = set()
    def dfs(i,j):
        visited.add((i,j))
        dir = [(1,0),(0,1),(-1,0),(0,-1)]
        for d1,d2 in dir:
            if 0 <= i + d1 < r and 0 <= j + d2 < c and grid[i+d1][j+d2] == '1' and (i+d1,j+d2) not in visited:
                dfs(i+d1,j+d2)
        return 
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '1' and (i,j) not in visited:
                res += 1
                dfs(i,j)     
    return res
    
