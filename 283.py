class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[i] = nums[index]
                i = i + 1

        for index in range(i, len(nums)):
            nums[index] = 0

        # return nums

#

nums = [0,1,0,3,12]
abject = Solution()
newNums = abject.moveZeroes(nums)
print(newNums)