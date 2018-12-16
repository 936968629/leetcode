class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        m = abs(n)
        if m == 0:
            return 1
        ans = 1.0
        while m:
            # 奇数
            if m & 1:
                ans *= x
            x *= x
            m = m >> 1
        return ans if n > 0 else 1/ans

sol = Solution()
res = sol.myPow(2, 7)
print(res)
