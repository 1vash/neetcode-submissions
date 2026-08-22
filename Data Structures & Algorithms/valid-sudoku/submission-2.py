class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # T: O(N^2); S: O(N)
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                tuple_box_id = (r // 3, c // 3) # tuple

                if val in rows[r] or val in cols[c] or val in boxes[tuple_box_id]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)

                boxes[tuple_box_id].add(val)

        return True


            

            
