class Solution:

    def xuanze(self, nums):
        for i in range(len(nums) - 1):
            k = i
            for j in range(i+1, len(nums)):
                if nums[k] > nums[j]:
                    k = j

            nums[i],nums[k] = nums[k], nums[i]

        return nums

nums = [1, 9, 10, 3, 100, 78, 28, 55, 88]
sol = Solution()
res = sol.xuanze(nums)
print(res)