import sys
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        queue = []
        queue.append([n, 0])
        visited = set()
        while queue:
            item = queue.pop(0)
            num = item[0]
            temp = item[1]

            if num == 0:
                return temp

            for i in range(1, n+1):
                shengyu = num - i * i
                if shengyu < 0:
                    break
                if shengyu not in visited:
                    queue.append([shengyu, temp+1])
                    visited.add(shengyu)
                i += 1
        """
        memo = [sys.maxsize for _ in range(n+1)]
        memo[0] = 1
        memo[1] = 1

        for i in range( n+1):
            j = 1
            while j*j <= i:
                if j*j == i:
                    memo[i] = 1
                    break
                else:
                    memo[i] = min(memo[i], memo[i-j*j]+1)
                j += 1
        # print(memo)
        return memo[n]

sol = Solution()
res = sol.numSquares(6730)
print(res)