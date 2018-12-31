class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [-1 for _ in range(n+1)]
        memo[1] = 1
        for i in range(1, n+1):
            for j in range(1, i):
                #拆分成j i-j
                memo[i] = max(j*memo[i-j], j*(i-j), memo[i])
        print(memo)
        return memo[n]







sol = Solution()
res = sol.integerBreak(11)