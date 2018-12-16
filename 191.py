class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        该n-1会把最右一边1变成0， 然后取与， 依次循环
        """
        count = 0

        while n:
            count += 1
            n = n & (n - 1)
        return count