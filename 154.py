class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while nums[left] >= nums[right]:
            mid = (left + right) // 2
            if left == right - 1:
                return nums[right]

            if nums[left] == nums[right] and nums[mid] == nums[left]:
                return self.minInOrder(nums, left, right)

            if nums[mid] >= nums[left]:
                left = mid
            elif nums[mid] <= nums[right]:
                right = mid
        return nums[left]

    def minInOrder(self, nums, left, right):
        minData = nums[left]
        while left <= right:
            if nums[left] < minData:
                minData = nums[left]
            left += 1
        return minData


        """
         start = 0
        end = len(nums) - 1
        last = nums[end]
        
        while (start < end):
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]: #last:
                start = mid + 1
            elif  nums[mid] < nums[end]: 
                end = mid 
            else:
                end -= 1
            
        return min(nums[start], nums[end])
        """

# [0,1,1,1,1]
nums = [3, 4, 5, 6, 1, 2]
# nums = [2, 0, 1, 1, 1]
nums = [1]
sol = Solution()
res = sol.findMin(nums)
print(res)
