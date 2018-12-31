class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if rows == 0 or cols == 0:
            return 0
        memo = [[0 for i in range(cols)] for _ in range(rows)]
        if obstacleGrid[0][0] == 1:
            return 0
        memo[0][0] = 1
        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 0:
                    if i + 1 < rows:  # 更新下面的方格
                        memo[i + 1][j] += memo[i][j]
                    if j + 1 < cols:  # 更新右边的方格
                        memo[i][j + 1] += memo[i][j]
                else:  # 如果有障碍物，则标记为0
                    memo[i][j] = 0
        print(memo)
        return memo[rows - 1][cols - 1]



grid = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
sol = Solution()
res = sol.uniquePathsWithObstacles(grid)
print(res)
