from collections import Counter
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        '''
        nums = sorted(nums)
        print(nums)
        for i in range(len(nums) - 1):
            j = i + 1
            if nums[i] == nums[j]:
                return True
            else:
                continue
        return False
        '''
        conterpar = Counter(nums)
        # print(conterpar)
        for k, v in conterpar.items():
            if v > 1:
                return True
        return False


        '''
        return len(set(nums)) != len(nums)
        '''

parsum = [1, 2, 3, 1]
sol = Solution()
res = sol.containsDuplicate(parsum)
print(res)
