"""
如果有4个物品[2, 3, 5, 7]

如果背包的大小为11，可以选择[2, 3, 5]装入背包，最多可以装满10的空间。

如果背包的大小为12，可以选择[2, 3, 7]装入背包，最多可以装满12的空间。

函数需要返回最多能装满的空间大小。
"""
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        """
        # O(n * W) space
        length = len(A)
        dp = [[-1 for i in range(m+1)] for _ in range(length) ]
        for i in range(length):
            dp[i][0] = 0
        for i in range(1, m+1):
            if i >= A[0]:
                dp[0][i] = A[0]
            else:
                dp[0][i] = 0
        for i in range(1, length):
            for j in range(1, m+1):
                if A[i] < j:
                    dp[i][j] = max(dp[i-1][j-A[i]] + A[i], dp[i-1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        print(dp)
        return dp[length-1][m]
        """
        length = len(A)
        dp = [0 for _ in range(m+1)]
        for i in range(length):
            for j in range(m, 0, -1):
                if j >= A[i]:
                    dp[j] = max(dp[j], dp[j-A[i]] + A[i])

        print(dp)
        return dp[m]


A = [6, 2, 3, 5, 7]
m = 13
sol = Solution()
res = sol.backPack(m, A)
print(res)