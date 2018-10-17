import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        # 数组排序
        nums.sort()
        # print(nums)
        print(nums[len(nums) - k])
        return nums[len(nums) - k]
        """
        # 堆
        heapList = nums[:k]
        print(heapList)
        heapq.heapify(heapList)
        print(heapList)
        for i in range(k, len(nums)):
            if nums[i] >= heapList[0]:
                heapq.heappushpop(heapList, nums[i])
        print(heapList)
        return heapList[0]


nums = [3, 2, 1, 5, 6, 4, 4, 6]
target = 3
sol = Solution()
sol.findKthLargest(nums, k=target)

