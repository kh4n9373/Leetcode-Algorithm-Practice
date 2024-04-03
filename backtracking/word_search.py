class Solution:
    def exist(self, board, word: str) -> bool:
        def backtrack(i, j, s, visited=set()):
            if s == len(word):
                return True
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] != word[s] or (i, j) in visited:
                return False
            visited.add((i, j))
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for d1, d2 in directions:
                if backtrack(i + d1, j + d2, s + 1, visited):
                    return True
            visited.remove((i, j))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False