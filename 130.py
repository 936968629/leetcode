class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                        self.dfs(board, i, j, rows, cols)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '-':
                    board[i][j] = 'O'

        print(board)
        # return board

    def dfs(self, board, i, j, rows, cols):
        move = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        board[i][j] = '-'
        for dx, dy in move:
            new_i = dx + i
            new_j = dy + j
            if 0 <= new_i < rows and 0 <= new_j < cols and board[new_i][new_j] == "O":
                self.dfs(board, new_i, new_j, rows, cols)


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
sol = Solution()
res = sol.solve(board)
print(res)
