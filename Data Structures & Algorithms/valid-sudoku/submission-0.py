from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                # if cell is "." → skip
                value = board[r][c]
                if value == ".":
                    continue
                else:
                    box_key = (r//3, c//3)
                    if value in rows[r] or value in cols[c] or value in boxes[box_key]:
                        return False
                    rows[r].add(value)
                    cols[c].add(value)
                    boxes[box_key].add(value)
                # otherwise:
                # compute box_key
                # check if digit already in rows[r], cols[c], or boxes[box_key]
                # if yes → return False
                # otherwise → add to all three
        
        return True
        