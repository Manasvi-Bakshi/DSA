class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = board[r][c]
                if(val in rows[r] or val in cols[c] or val in square[(r//3,c//3)]):
                    return False
                rows[r].add(val)
                cols[c].add(val)
                square[r//3,c//3].add(val)
        return True


        