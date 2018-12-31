class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        f(n) = num[0] + f(n-2)
        f(n) = num[1] + f(n-3)
        """
        # O(n)空间复杂度
        """
        maps = {}
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])
        maps[1] = nums[0]
        maps[2] = max(nums[0], nums[1])
        i = 3
        while i <= length:
            maps[i] = max(maps[i - 2] + nums[i-1], maps[i - 1])
            i += 1
        print(maps)
        return maps[length]
        """
        # O(1)空间复杂度
        pre = 0
        ppre = 0
        length = len(nums)
        for i in range(length):
            if nums[i] + ppre >= pre:
                ppre, pre = pre, nums[i] + ppre
            else:
                ppre = pre
        return pre



nums = [2, 7, 9, 3, 1]
sol = Solution()
res = sol.rob(nums)
print(res)
