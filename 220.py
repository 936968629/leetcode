from collections import OrderedDict
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        '''
        if k < 1 or t < 0:
            return False
        dic = OrderedDict()
        for n in nums:
            key = n if not t else n // t
            for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            if len(dic) == k:
                dic.popitem(False)
            dic[key] = n
        return False
        '''

        lenth = len(nums)
        a = set()
        for i in range(lenth):
            if t == 0:
                if nums[i] in a:
                    return True
            else:
                for atem in a:
                    if abs(nums[i] - atem) <= t:
                        return True
            a.add(nums[i])
            if len(a) == k + 1:
                a.remove(nums[i - k])
        return False
nums = [1, 2, 3, 1]
k = 3
t = 0
sol = Solution()
res = sol.containsNearbyAlmostDuplicate(nums, k, t)
print(res)