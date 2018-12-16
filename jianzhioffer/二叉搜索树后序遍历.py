class Solution:
    def validateStackSequences(self, nums):

        length = len(nums)

        if length == 0:
            return False

        root = nums[-1]
        i = 0
        while i < length - 1:
            if nums[i] > root:
                break
            i += 1
        j = i
        while j < length - 1:
            if nums[j] < root:
                return False
            j += 1
        # print(i)

        left = True
        if i > 0:
            left = self.validateStackSequences(nums[:i])
        right = True
        if i < length - 1:
            right = self.validateStackSequences(nums[i:length-1])

        return left and right


nums = [5,7,6,9,11,10,8]
sol = Solution()
res = sol.validateStackSequences(nums)
print(res)

