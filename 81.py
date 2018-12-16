class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        length = len(nums)
        start = 0
        end = length - 1
        if length == 0:
            return False
        while start <= end:
            mid = (start + end) >> 1
            if nums[mid] == target:
                return True
            elif nums[mid] < nums[end]:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif nums[mid] > nums[end]:
                if nums[mid] > target and target >= nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                end -= 1

        return False




nums = [2,5,6,0,0,1,2]
sol = Solution()
res = sol.search(nums, 2)
print(res)