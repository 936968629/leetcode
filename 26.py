class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        j = 1
        while i < len(nums):
            if j >= len(nums):
                break
            if nums[i] == nums[j]:
                del nums[j]
            else:
                i += 1
                j += 1

        print(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
sol.removeDuplicates(nums)