class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        item = []
        shengyu = [0 for i in range(len(nums))]

        self.helper(nums, item, shengyu)

        return self.res

    def helper(self, nums, item, shengyu):
        if len(nums) == len(item):
            self.res.append(item[:])
            return
        for i in range(len(nums)):
            if not shengyu[i]:
                shengyu[i] = 1
                item.append(nums[i])
                self.helper(nums, item, shengyu)
                item.pop()
                shengyu[i] = 0


nums = [1, 2, 3]
sol = Solution()
res = sol.permute(nums)
print(res)