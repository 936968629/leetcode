class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def partition(self, array, left, right):
        if left >= right:
            return

        key = array[left]
        while left < right:
            while left < right and array[right] > key:
                right -= 1
            array[left] = array[right]
            while left < right and array[left] <= key:
                left += 1
            array[right] = array[left]
        array[right] = key
        return right

    def kthLargestElement(self, k, A):
        n = len(A)
        if n < k or k <= 0 or n <= 0:
            return None
        left = 0
        right = n - 1

        while left < right:
            qvoit = self.partition(A, left, right)
            if qvoit < n - k:
                left = qvoit + 1
            elif qvoit > n - k:
                right = qvoit - 1
            else:
                return A[qvoit]
        return A[left]


sol = Solution()
res = sol.kthLargestElement()
