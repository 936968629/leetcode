class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) space
        # dp[i] 代表的是以nums[i]数结尾的最大子序列数组和
        if len(nums) == 0:
            return 0
        dp = {}
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            res = max(res, dp[i])
        return res

nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
res = sol.maxSubArray(nums)
print(res)