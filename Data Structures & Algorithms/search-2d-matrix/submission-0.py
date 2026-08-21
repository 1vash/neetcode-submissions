class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # T=O(log(m * n)), M=O(1)

        ROWS, COLS = len(matrix), len(matrix[0])

        # BS in matrix (vertical direction), to find the row 
        top_row, bot_row = 0, ROWS - 1
            # top_row  1  2  3  4
            #          5  6  7  8
            # bot_row  9 10 11 12
        while top_row <= bot_row:
            mid_row = (top_row + bot_row) // 2
            
            mid_row_start_val = matrix[mid_row][0]
            mid_row_end_val = matrix[mid_row][-1]

            if mid_row_end_val < target:
                # target is higher than biggest value in the row, GO DOWN
                top_row = mid_row + 1
            elif mid_row_start_val > target:
                # target is lower than lowest value in the row, GO UP
                bot_row = mid_row - 1
            else:
                # we have to find a row where target is between mid_row values  
                break

        if not top_row <= bot_row:
            return False 
        
        # potential row is found, it's mid_row
        # row   1  2  3  4
        row = mid_row

        print('Row:', row)

        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] > target:
                right = mid -1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True
        
        return False
        



