class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 位运算
        return n > 0 and ( n & n-1 ) == 0



num = 32
sol = Solution()
res = sol.isPowerOfTwo(num)
print(res)