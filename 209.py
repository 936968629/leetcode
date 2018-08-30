class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # [l, ... , r]
        l = 0
        r = -1
        sum = 0
        res = len(nums) + 1
        while l < len(nums):
            if sum < s and r < len(nums) - 1:
                r += 1
                sum += nums[r]
            else:
                sum -= nums[l]
                l += 1
            if sum >= s:
                res = min(res, r-l+1)
        if res == len(nums) + 1:
            res = 0
        print(res)
        return res

        '''
        while r < len(nums):
            if sum < s:
                if r < len(nums) - 1:
                    r += 1
                    sum += nums[r]
                else:
                    r += 1
            else:
                res = min(res, r - l + 1)
                l += 1
                sum -= nums[l - 1]
        if res == len(nums) + 1:
            res = 0
        print(res)
        return res
        '''

# numArr = [2, 3, 1, 2, 4, 3]
# se = 7
# se = 1000
numArr = [1,1]

se = 3
sol = Solution()
sol.minSubArrayLen(se, numArr)
