class Solution(object):

    def takeFirst(elem):
        return elem[0]

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        length = len(nums)
        if length == 0:
            return ''
        nums.sort()
        # print(nums)



# nums = [10, 2]
nums = [10, 2, 9, 92]
sol = Solution()
sol.largestNumber(nums=nums)

