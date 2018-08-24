class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) -1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                print((i, j))
                return (i+1, j+1)
        print((-1, -1))
        return (-1, -1)


oldNums = [2, 7, 11, 15]
k = 3
sol = Solution()
Solution.twoSum(sol, oldNums, k)