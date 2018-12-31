class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])
        maps1 = self.single_rob(0, length-1, nums)  # 不抢最后一个房间
        maps2 = self.single_rob(1, length, nums)  # 不抢第一个房间

        return max(maps1, maps2)

    def single_rob(self, first,last,nums):
        pre = 0
        ppre = 0
        for i in range(first,last):
            if ppre+nums[i] >= pre:
                ppre,pre = pre, ppre+nums[i]
            else:
                ppre = pre
        return pre


nums = [1, 2, 3, 5]
sol = Solution()
res = sol.rob(nums)
print(res)
