# 从顶部到底部的最大和值
class Solution:

    def numberTower(self, nums):
        rows = len(nums)
        cols = len(nums[rows-1])
        if rows == 0 or cols == 0:
            return None
        maxNum =[ [0 for i in range(cols) ] for j in range(rows) ]
        for i in range(cols):
            maxNum[rows-1][i] = nums[rows-1][i]

        for i in range(rows-2, -1, -1):
            for j in range(len(nums[i])):
                maxNum[i][j] = max(maxNum[i+1][j]+nums[i][j], maxNum[i+1][j+1]+nums[i][j])

        print(maxNum)
        return maxNum[0][0]


nums = [
    [7],
    [3,8],
    [8,1,0],
    [2,7,4,4],
    [4,5,2,6,5]
]
sol = Solution()
res = sol.numberTower(nums)
print(res)