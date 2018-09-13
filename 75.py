class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        newnum = nums
        i = 0
        count = [0 for i in range(3)]
        while(i < len(nums)):
            count[nums[i]] += 1
            i += 1
        index = 0
        for ii in range(count[0]):
            nums[index] = 0
            index += 1
        for ii in range(count[1]):
            nums[index] =1
            index += 1
        for ii in range(count[2]):
            nums[index] = 2
            index += 1
        print(newnum)
        # return nums

numsArr = [2,0,2,1,1,0]
sol = Solution()
sol.sortColors(numsArr)