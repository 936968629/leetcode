class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        results = []
        tmp = []
        self.helper(results, tmp, 0)
        return results

    def helper(self, results, tmp, step):
        if step == len(self.nums):
            results.append(tmp[:])
            return

        self.helper(results, tmp, step + 1)
        tmp.append(self.nums[step])
        self.helper(results, tmp, step + 1)
        tmp.pop()



nums = [1, 2, 3]
sol = Solution()
res = sol.subsets(nums)
print(res)
