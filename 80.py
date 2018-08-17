class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        count = 0
        while j < len(nums):
            if nums[i] == nums[j]:
                count += 1
                if count >= 2:
                    del nums[j]
                else:
                    i += 1
                    j += 1
            else:
                i += 1
                j += 1
                count = 0

        print(nums)

numsArr = [0,0,1,1,1,1,2,3,3]
sol = Solution()
sol.removeDuplicates(numsArr)