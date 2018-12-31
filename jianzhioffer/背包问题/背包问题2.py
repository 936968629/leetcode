class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, w, v, C):
        # O(C * len(w)) space
        """
        length = len(w)
        memo = [[0 for i in range(C+1)] for _ in range(length)]
        for i in range(C+1):
            if w[0] <= i:
                memo[0][i] = v[0]

        for i in range(1, length):
            for j in range(C+1):
                if j >= w[i]:
                    memo[i][j] = max(memo[i-1][j-w[i]] + v[i], memo[i-1][j])
                else:
                    memo[i][j] = memo[i-1][j]
        print(memo)
        """
        #
        """
        length = len(w)
        memo = [[0 for i in range(C + 1)] for _ in range(2)]
        for i in range(C + 1):
            if w[0] <= i:
                memo[0][i] = v[0]

        for i in range(1, length):
            for j in range(C + 1):
                memo[i%2][j] = memo[(i-1)%2][j]
                if j >= w[i]:
                    memo[i%2][j] = max(memo[(i-1)%2][j - w[i]] + v[i], memo[i%2][j])
        print(memo)
        """
        length = len(w)
        memo = [0 for i in range(C + 1)]
        for i in range(C + 1):
            if w[0] <= i:
                memo[i] = v[0]

        for i in range(1, length):
            for j in range(C, w[i]-1, -1):
                memo[j] = max(memo[j], memo[j-w[i]] + v[i])

        print(memo)

w = [2, 3, 5, 7]
v = [1, 5, 2, 4]
C = 10
sol = Solution()
res = sol.backPack(w, v ,C)
print(res)
