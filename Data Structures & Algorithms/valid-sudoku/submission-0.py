class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        print('HERE1')


        # Row Validity check
        for row_idx in range(9):
            unq_row = set()
            for row_val in board[row_idx]: 
                if row_val == '.':
                    continue
                if row_val in unq_row:
                    return False
                unq_row.add(row_val)        
        
        print('HERE2')


        # Col Validity check
        # for each col we try different rows
        for col_idx in range(9):
            unq_col = set()
            for row_idx in range(9):
                col_val = board[row_idx][col_idx]
                print(col_val)
                if col_val == '.':
                    continue
                if col_val in unq_col:
                    return False
                unq_col.add(col_val)   
            print('-------------')
 
        
        """          
            0 0 0 1 1 1 2 2 2 [COL_ID]
        0  0 1 2 3 4 5 6 7 8
        0  1
        0  2
        1  3
        1  4       [1,1] -> which is the 4-th block_id
        1  5
        2  6
        2  7
        2  8
        [ROW_ID]

        ROW_ID = row / 3
        COL_ID = col / 3

        by having board[ROW_ID][COL_ID] we can get cell's address
        """

        print('HERE3')

        unq_block = defaultdict(set)
        for row_idx in range(9):
            for col_idx in  range(9):
                board_val = board[row_idx][col_idx]
                if board_val == '.':
                    continue
                ROW_ID, COL_ID = row_idx // 3, col_idx // 3
                BLOCK_ADDR = (ROW_ID, COL_ID)
                if board_val in unq_block[BLOCK_ADDR]:
                    return False
                unq_block[BLOCK_ADDR].add(board_val)

        return True
        


