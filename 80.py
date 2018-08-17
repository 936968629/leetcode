class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # i = 0
        # j = 1
        # count = 0
        # while j < len(nums):
        #     if nums[i] == nums[j]:
        #         count += 1
        #         if count >= 2:
        #             del nums[j]
        #         else:
        #             i += 1
        #             j += 1
        #     else:
        #         i += 1
        #         j += 1
        #         count = 0
        #
        # print(nums)

        '''
        or
        '''

        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        print(i)
        return i


numsArr = [0,0,1,1,1,1,2,3,3]
sol = Solution()
sol.removeDuplicates(numsArr)