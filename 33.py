class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        return self.rotatedBinarySearch(nums, 0, len(nums) - 1, target)

    def rotatedBinarySearch(self, nums, left, right, target):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] < nums[right]:
            if nums[mid] < target:
                return self.rotatedBinarySearch(nums, mid, right, target)
            else:
                return self.rotatedBinarySearch(nums, left, mid, target)
        else:
            leftside = self.rotatedBinarySearch(nums, mid + 1, right, target)
            rightside = self.rotatedBinarySearch(nums, mid + 1, right, target)

            if leftside != -1:
                return leftside
            else:
                return rightside
        """

        length = len(nums)
        if length == 0:
            return -1
        start = 0
        end = length - 1
        while start <= end:
            mid = (start + end) >> 1
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[end]:
                if nums[mid] < target and nums[end] >= target:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] > target and nums[start] <= target:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 5
sol = Solution()
res = sol.search(nums, target)
print(res)
