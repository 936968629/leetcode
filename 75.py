class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = [0 for i in range(3)]
        while(i < len(nums)):
            count[nums[i]] += 1
            i += 1

        print(count)


numsArr = [2,0,2,1,1,0]
sol = Solution()
sol.sortColors(numsArr)