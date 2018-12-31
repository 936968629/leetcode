class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        if rows == 0 or cols == 0:
            return 0
        memo = [[0 for _ in range(cols)] for i in range(rows)]
        memo[0][0] = grid[0][0]
        for i in range(1, cols):
            memo[0][i] = grid[0][i] + memo[0][i-1]
        for i in range(1, rows):
            memo[i][0] = grid[i][0] + memo[i-1][0]

        for i in range(1, rows):
            for j in range(1, cols):
                memo[i][j] = min(memo[i - 1][j] + grid[i][j], memo[i][j - 1] + grid[i][j])
        print(memo)
        print(memo[rows-1][cols-1])
        return memo[rows-1][cols-1]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
sol = Solution()
res = sol.minPathSum(grid)
print(res)
