
# class Solution:
#
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#
#         rows = len(board)
#         cols = len(board[0])
#         currnt_word = ''
#         self.visited = set()
#         self.found = False
#         for i in range(rows):
#             for j in range(cols):
#                 if (i, j) not in self.visited and self.found is False:
#                     self.helper(board, currnt_word, i, j, word, rows, cols)
#         return self.found
#
#     def helper(self, board, current_word, i, j, word, rows, cols):
#
#
#         if current_word == word:
#             self.found = True
#             return
#
#         move = [(0,1), (1,0), (0,-1), (-1,0)]
#         for dx, dy in move:
#             if (word.startswith(current_word) and 0 <= i + dx < rows and 0 <= j + dy < cols and
#                     (i + dx, j + dy) not in self.visited and not self.found):
#                 self.visited.add((i, j))
#                 c = board[i][j]
#                 current_word += c
#                 self.helper(board, current_word, i + dx, j + dy, word, rows, cols)
#         current_word = current_word[:-1]
#         self.visited.remove((i, j))


class Solution:
    def _searchWord(self, board, word, index, i, j, rows, cols, visited):
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if index == len(word) - 1:
            return board[i][j] == word[index]
        if board[i][j] == word[index]:
            visited[i][j] = True
            for dx, dy in move:
                new_i = i + dx
                new_j = j + dy
                if 0 <= new_i < rows and 0 <= new_j < cols and not visited[new_i][new_j]:
                    if self._searchWord(board, word, index + 1, new_i, new_j,rows, cols, visited):
                        return True
            visited[i][j] = False
        return False


    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        # visited = [[False for i in range(rows)] for _ in range(cols)]
        visited = list()

        for i in board:
            t = list()
            for _ in i:
                t.append(False)

            visited.append(t)

        for i, val in enumerate(board):
            for j, _ in enumerate(val):
                if self._searchWord(board, word, 0, i, j, rows, cols, visited):
                    print(visited)
                    return True

        return False

board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
# board = [
#     ['a']
# ]
word = "ABCCED"
# word = 'ab'
sol = Solution()
res = sol.exist(board, word)
print(res)
