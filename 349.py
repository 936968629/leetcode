class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        print(list(nums1 & nums2))
        return list(nums1 & nums2)


numsOne = [4, 9, 5, 1]
numTwo = [9, 4, 9, 8, 4]
sol = Solution()
sol.intersection(numsOne, numTwo)
