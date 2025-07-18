class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        def dfs(i, j):
            if(i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != '1'):
                return
            grid[i][j] = '0'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == '1'):
                    dfs(i, j)
                    num_islands += 1
        return num_islands