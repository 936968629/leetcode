class Solution:

    def maopao(self, nums):
        

        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j+1] < nums[j]:
                    nums[j+1],nums[j] = nums[j], nums[j+1]

        return nums


nums = [1, 9, 10, 3, 100, 78, 28, 55, 88]
sol = Solution()
res = sol.maopao(nums)
print(res)