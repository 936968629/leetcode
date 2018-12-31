class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if len(s[i - 2:i]) == 2 and '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]
        print(dp)
        return dp[n]

s = "1022"
s = "226"
s = "0"
sol = Solution()
res = sol.numDecodings(s)
print(res)