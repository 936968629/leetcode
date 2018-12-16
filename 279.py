class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
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


sol = Solution()
res = sol.numSquares(13)
print(res)