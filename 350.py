class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        result = []
        for item in nums1:
            if item in hashmap:
                hashmap[item] += 1
            else:
                hashmap[item] = 1

        for item in nums2:
            if item in hashmap.keys():
                if hashmap[item] > 0:
                    hashmap[item] -= 1
                    result.append(item)
                else:
                    hashmap.pop(item)
        print(result)
        return result


numOne = [1, 2, 2, 1]
numTwo = [2, 2, 1]
sol = Solution()
sol.intersect(numOne, numTwo)
