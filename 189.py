class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        print(nums)
        self.reverse(nums, 0, n - 1)
        print(nums)
        self.reverse(nums, n, len(nums) - 1)
        return nums

    def reverse(self, arr, start, stop):
        while start < stop:
            arr[start], arr[stop] = arr[stop], arr[start]
            start += 1
            stop -= 1


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
sol = Solution()
res = sol.rotate(nums, k)
print(res)
