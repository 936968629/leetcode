class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        if n == 1 or n == 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        """
        maps = {}
        maps[1] = 1
        maps[2] = 2
        i = 3
        while i <= n:
            maps[i] = maps[i - 1] + maps[i - 2]
            i += 1

        return maps[n]