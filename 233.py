class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        超时
        
        result = 0
        for i in range(n+1):
            while i:
                if i % 10 == 1:
                    result += 1
                i = i // 10
        return result
        """

        if n <= 0:
            return 0
        if 1 <= n <= 9:
            return 1
            # compute the first bit
        head, level = n, 1
        while head > 9:
            level *= 10
            head //= 10
        # if the first bit is 1
        # like 191, divide it into (0-99), (0-91) and the first bit in (100, 101, 1.., 191)
        if head == 1:
            return self.countDigitOne(level - 1) + self.countDigitOne(n - level) + n - level + 1
        # like 491, divide it into (0-99), (100-199), (200-299, 300-399) and (400-491)
        return (head) * self.countDigitOne(level - 1) + self.countDigitOne(n - head * level) + level

n = 13
sol = Solution()
res = sol.countDigitOne(n)
print(res)