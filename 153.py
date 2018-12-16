class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while nums[left] >= nums[right]:
            mid = (left + right) // 2
            if left == right - 1:
                return nums[right]
            if nums[mid] >= nums[left]:
                left = mid
            elif nums[mid] <= nums[right]:
                right = mid
        return nums[left]

# [0,1,1,1,1]
nums = [3, 4, 5, 6, 1, 2]
# nums = [2, 0, 1, 1, 1]
nums = [1]
sol = Solution()
res = sol.findMin(nums)
print(res)
