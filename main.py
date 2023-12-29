# Sudoku Solver by Abdul Basit Tonmoy

from pprint import pprint


def next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    
    return None, None


def is_valid(puzzle, row, col, guess):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False

    # Sudoku rule: number must not be repeated in the row, column, or 3x3 square that it appears in



    #checking rows
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    #checking cols
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    #checking 3x3 small metrices
    row_starts_for_small_metrices = (row // 3)*3
    col_starts_for_small_metrices = (col//3)*3

    for r in range(row_starts_for_small_metrices, row_starts_for_small_metrices+3):
        for c in range(col_starts_for_small_metrices, col_starts_for_small_metrices+3):
            if puzzle[r][c] == guess:
                return False

    # passes all the checks, so valid
    return True




def solve_sudoku(puzzle):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)


    row, col = next_empty(puzzle)
    if row is None:
        return True
    for guess in range(1, 10):
        # validity of the guess
        if is_valid(puzzle, row, col, guess):
            # if the guess is valid, put the guess in that index
            puzzle[row][col] = guess
            #recursively calling the function
            if solve_sudoku(puzzle):
                return True

    # if the guess wasn't right, going back to/ backtracking to -1
        puzzle[row][col] = -1  # reset the value

    #  after trying everything, if still can't find the solution, then there is no solution aka UNSOLVABLE!!!
    return False



if __name__ == '__main__':
    example_board = [
        [-1, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
