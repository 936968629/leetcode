class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_set = set()
        result = []
        self.helper(nums, result, [], 0, res_set)
        print(res_set)
        return result

    def helper(self, nums, result, temp, i, res_set):
        if len(nums) == i:
            sortedTemp = sorted(temp)
            if tuple(sortedTemp) not in res_set:
                result.append(temp[:])
            res_set.add(tuple(sortedTemp))
            return

        self.helper(nums, result, temp, i+1, res_set)
        temp.append(nums[i])
        self.helper(nums, result, temp, i+1, res_set)
        temp.pop()


nums = [1, 2, 2]
nums = [4, 4, 4, 1, 4]
sol = Solution()
res = sol.subsetsWithDup(nums)
print(res)