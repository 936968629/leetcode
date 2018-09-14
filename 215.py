class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        # print(nums)
        print(nums[len(nums) - k])
        return nums[len(nums) - k]


nums = [3, 2, 1, 5, 6, 4, 4, 6]
target = 3
sol = Solution()
sol.findKthLargest(nums, k=target)

