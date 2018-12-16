class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        length = len(A)
        if length == 0:
            return []
        i = 0
        j = length - 1
        while i < j:
            # 偶数
            if self.func(A[i]):
                i += 1
            else:
                A[i], A[j] = A[j], A[i]
                j -= 1

        return A

    def func(self, number):
        # return number % 2 == 0
        return number < 0


num = [3, 1, -2, 4]
sol = Solution()
res = sol.sortArrayByParity(num)
print(res)