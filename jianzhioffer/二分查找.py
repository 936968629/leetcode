# 二分查找必须有序
class Solution:
    def find(self, nums, target):
        if len(nums) == 0:
            return False
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
               right = middle - 1
            if nums[middle] < target:
                left = middle + 1
            if nums[middle] == target:
                return True
        return False


nums = [1, 8, 11, 4, 3, 5, 7]
sol = Solution()
res = sol.find(nums, 4)
print(res)