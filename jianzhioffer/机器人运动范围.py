class Solution:

    def getSum(self, i):
        sum = 0
        while i > 0:
            sum += i % 10
            i = i // 10
        return sum

    def findgrid(self, threshold, rows, cols, matrix, i, j):
        matrix[i][j] = 1
        if self.getSum(i) + self.getSum(j) > threshold:
            return

        if 0 <= i < rows and 0 <= j < cols and self.getSum(i) + self.getSum(j) <= threshold and matrix[i][j] == 0:

            self.count += 1
            move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in move:
                self.findgrid(threshold, rows, cols, matrix, i + dx, j + dy)
        matrix[i][j] = 0

    def movingCount(self, threshold, rows, cols):
        # write code here
        self.count = 0
        matrix = [[0 for i in range(cols)] for j in range(rows)]
        self.findgrid(threshold, rows, cols, matrix, 0, 0)
        print(matrix)
        return self.count


sol = Solution()
res = sol.movingCount(2, 4, 4)
print(res)
