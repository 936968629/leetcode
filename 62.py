class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        memo = [[1 for i in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                memo[i][j] = memo[i-1][j] + memo[i][j-1]
        return memo[n-1][m-1]
