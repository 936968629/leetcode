class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        rows = len(triangle)
        cols = len(triangle[rows - 1])
        if rows == 0 or cols == 0:
            return None
        minNum = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(cols):
            minNum[rows - 1][i] = triangle[rows - 1][i]

        for i in range(rows - 2, -1, -1):
            for j in range(len(triangle[i])):
                minNum[i][j] = min(minNum[i + 1][j] + triangle[i][j], minNum[i + 1][j + 1] + triangle[i][j])

        # print(minNum)
        return minNum[0][0]