class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 1
        end = len(nums) - 1

        while end >= start:
            mid = (start + end) // 2
            count = self.countRange(nums, start, mid)

            if end == start:
                return end

            if count > mid - start + 1:
                end = mid
            else:
                start = mid + 1

    @staticmethod
    def countRange(nums, start, end):
        length = len(nums)
        count = 0
        for i in range(length):
            if nums[i] >= start and nums[i] <= end:
                count += 1
        return count


nums = [3, 1, 3, 4, 2, 5]
# nums = [4,3,1,4,2]
sol = Solution()
res = sol.findDuplicate(nums)
print(res)
