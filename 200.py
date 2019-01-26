class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        visited = [[False for i in range(cols)] for _ in range(rows)]

        self.count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    self.dfs(grid, rows, cols, i, j, visited)
                    self.count += 1

        return self.count

    def dfs(self, grid, rows, cols, i, j, visited):
        move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited[i][j] = True
        for dx, dy in move:
            new_i = dx + i
            new_j = dy + j
            if 0 <= new_i < rows and 0 <= new_j < cols and not visited[new_i][new_j] and grid[new_i][new_j] == "1":
                self.dfs(grid, rows, cols, new_i, new_j, visited)


grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
grid = []
sol = Solution()
res = sol.numIslands(grid)
print(res)
