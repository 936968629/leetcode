

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not isinstance(x, int):
            return False
        count = 1
        if x < 0:
            count = -1
        x_ = int(str(abs(x))[::-1]) * count
        if x_ < -2 ** 31 or x_ > 2 ** 31 - 1:
            return 0
        print(x_)
        return x_


edigit = -1234
sol = Solution()
sol.reverse(edigit)
# str = 'qwer'
# print(str[::-1])
