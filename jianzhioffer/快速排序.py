# 剑指offer80页 207
class Solution:
    def fast(self, nums):

        self.quickSort(nums, 0 ,len(nums)-1)
        print(nums)

    def quickSort(self, L, low, high):
        i = low
        j = high
        if i >= j:
            return
        key = L[i]
        while i < j:
            while i < j and L[j] >= key:  # 从后向前找比key小的值
                j -= 1
            L[i] = L[j]  # 把比key小的值移到key在的位置
            while i < j and L[i] <= key:  # 从前向后找比key大的值
                i += 1
            L[j] = L[i]  # 把比key大的值移到刚找出的比key小的值的位置
        L[i] = key  # 这时的i左右分别为比key小和大的值，key移到i处
        self.quickSort(L, low, i - 1)  # 继续排前一部分
        self.quickSort(L, j + 1, high)  # 继续排后一部分
        return


nums = [1, 7, 89, 2, 78, 100, 67, 45]
sol = Solution()
res = sol.fast(nums)
print(res)