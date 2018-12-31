class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        memo = [1 for _ in range(length)]
        for i in range(1, length):
            for j in range(i):
                if nums[i] >= nums[j]:
                    memo[i] = max(memo[i], memo[j]+1)


        print(max(memo))


nums = [10,9,2,5,3,7,101,18]
sol = Solution()
res = sol.lengthOfLIS(nums)
print(res)