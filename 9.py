class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if not isinstance(x, int):
            print(False)
            return False
        x = str(x)
        i = 0
        j = len(x) - 1
        while i < j:
            if x[i] == x[j]:
                i += 1
                j -= 1
            else:
                print(False)
                return False
        print(True)
        return True

num = 181
sol = Solution()
sol.isPalindrome(num)
