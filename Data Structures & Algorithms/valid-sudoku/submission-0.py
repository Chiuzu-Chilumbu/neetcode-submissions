class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # declare row, col, boxes sets
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Iterate through the board
        for row in range(9):
            for col in range(9):
                # obtain current number
                num = board[row][col]

                # if empty we continue 
                if num == '.':
                    continue

                # obtain the position of the sub box 
                # in relation to overal grid
                box_index = (row // 3) * 3 + (col // 3)

                # check if the num exists in other sets
                if (num in rows[row] or num in cols[col] or num in boxes[box_index]):
                    return False 

                # otherwise we add the nuumber to respective rows
                rows[row].add(num)
                cols[col].add(num)
                boxes[box_index].add(num)

        return True
                




