class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 2
        dic = {}
        lens = len(nums)
        res = set()
        #先取前两个数之和以及下标
        for i in range(lens - 1):
            for j in range(i+1, lens):
                key = nums[i] + nums[j]
                if key not in dic:
                    dic[key] = [(i, j)]
                else:
                    dic[key].append( (i,j) )
        #取最后一个数
        for i in range(2, lens):
            diff = target - nums[i]
            if diff in dic:
                for index in dic[diff]:
                    #最后一个数下标必定大于前两个下标
                    if index[1] < i:
                        #整理重合的元祖
                        mylist = [nums[index[0]], nums[index[1]], nums[i] ]
                        mylist.sort()
                        mytuple = tuple(mylist)
                        res.add( mytuple )
        print([list(i) for i in res])
        return [list(i) for i in res]


oldNums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
sol.threeSum(oldNums)