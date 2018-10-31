class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        resList = []
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[i] == nums[nums[i]-1]:
                    resList.append(nums[i])
                    break
                    # return True
                # nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
                tem = nums[i]
                nums[i] = nums[tem-1]
                nums[tem - 1] = tem
        print(nums)
        print(resList)
        """
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res

numList = [4, 3, 2, 7, 8, 2, 3, 1]
sol = Solution()
res = sol.findDuplicates(numList)
print(res)
