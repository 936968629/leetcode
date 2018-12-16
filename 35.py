class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        start = 0
        end = length - 1
        res = 0
        while start <= end:
            mid = (start + end) >> 1
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
                res = mid
            else:
                start = mid + 1
                res = mid + 1
        return res



