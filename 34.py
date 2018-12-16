class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        length = len(nums)
        start = 0
        end = length - 1
        if length == 0:
            return [-1, -1]
        while start <= end:
            mid = (start + end) >> 1
            if nums[mid] == target:
                #查找做左端点和右端点
                left, right = mid, mid
                while left > 0:
                    if nums[left-1] == target:
                        left -= 1
                    else:
                        break
                while right < length-1:
                    if nums[right + 1] == target:
                        right += 1
                    else:
                        break
                return [left, right]
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return [-1, -1]
        """
        length = len(nums)
        if length == 0:
            return [-1, -1]
        left = self.left_num(nums, target)
        right = self.right_nums(nums, target)
        return [left, right]

    def left_num(self, nums, target):
        length = len(nums)
        start = 0
        end = length - 1
        while start <= end:
            mid = (start + end) >> 1
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] < target:
                    return mid
                end = mid - 1
                continue
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def right_nums(self, nums, target):
        length = len(nums)
        start = 0
        end = length - 1
        while start <= end:
            mid = (start + end) >> 1
            if nums[mid] == target:
                if mid == length -1 or nums[mid+1] > target:
                    return mid
                start = mid + 1
                continue
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

nums = [5,7,7,8,8,10]
target = 8
sol = Solution()
res = sol.searchRange(nums, target)
print(res)