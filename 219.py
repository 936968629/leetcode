class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        '''
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                if i - d[nums[i]] <= k:
                    return True
                else:
                    d[nums[i]] = i
            else:
                d[nums[i]] = i
        return False
        '''

        # [l , l+k]区间内查找是否存在相等的元素
        # find_map = {}
        # for i, v in enumerate(nums):
        #     if v in find_map and i - find_map[v] <= k:
        #         return True
        #     find_map[v] = i
        # print(find_map)
        # return False

        #使用set
        find_map = set()
        for i in range(nums):
            if i in find_map:
                return True

            if len(find_map) == k+1:
                find_map.remove(nums[i - k])
        return False

nums = [1, 2, 3, 1, 7, 8]
k = 3
sol = Solution()
res = sol.containsNearbyDuplicate(nums, k)
print(res)
