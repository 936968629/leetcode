import sys
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #dp[i]表示装满i数量所需要的最少硬币数，状态转移方程为dp[i] = math.min(dp[i], dp[i - k] + 1), 满足i >= k的条件即可
        dp = [sys.maxsize for i in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                        dp[i] = min(dp[i-coins[j]] + 1, dp[i])

        print(dp)
        if dp[amount] == sys.maxsize:
            return -1
        return dp[amount]


coins = [484,313,214,492,452,10,218,103,16]

amount = 2188
sol = Solution()
res = sol.coinChange(coins, amount)
print(res)