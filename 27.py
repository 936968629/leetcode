class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # for index in reversed(range(len(nums))):
        #     if nums[index] == val:
        #         nums.remove(nums[index])

        # 删除list某一元素后对应的键值也会改变

        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        print(nums)


numArr = [0, 1, 2, 2, 3, 0, 4, 2]
so = Solution()
so.removeElement(numArr, 2)
