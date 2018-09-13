class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        nums.sort()
        res = nums[0] + nums[1] + nums[len(nums) - 1]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s-target) < abs(res - target):
                    res = s
                if s == target:
                    return target
                elif s > target:
                    k -= 1
                else:
                    j += 1
        print(res)
        return res


nums = [-1, 2, 1, -4]
target = 1
sol = Solution()
sol.threeSumClosest(nums, target)