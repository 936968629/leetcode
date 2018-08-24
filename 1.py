class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums[i+1:]:
                # print(i, nums[i+1:].index(diff) + 1 + i)
                return (i, nums[i+1:].index(diff) + 1 + i)
        # print(-1, -1)
        return (-1, -1)

num = [2, 7, 4, 9]
target = 14
sol = Solution()
sol.twoSum(num, target)