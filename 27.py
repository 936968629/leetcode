class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        for index in reversed(range(len(nums))):
            if nums[index] == val:
                nums.remove(nums[index])


        print(nums)

numArr = [0,1,2,2,3,0,4,2]
so = Solution()
so.removeElement(numArr, 2)
