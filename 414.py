class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        print(nums)
        if len(nums) < 3:
            return max(nums)
        for i in range(2):
            nums.remove(max(nums))
        print(nums)
        print(max(nums))
        return max(nums)

numRow = [2, 2, 3, 1]
sol = Solution()
sol.thirdMax(nums=numRow)