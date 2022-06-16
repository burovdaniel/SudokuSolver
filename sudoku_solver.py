'''' Solves sudoku Problems given in txt formant as a command line argument
'''
import sys
import re

def check_file():
    ''' Checks if command is correct
        and that is tct file
    '''
    if len(sys.argv) != 2 or re.search(".txt$", sys.argv[1]) is None:
        print("please provide the text file with the Sudoku puzzle")
        sys.exit()
    else:
        pass

def parser():
    ''' Parses the input txt puzzle into an int 2s 9x9 array
        returns the parsed puzzle as a global
        *it assumes given a 9x9 grid
    '''
    #opens the input puzzle and saves as list of the string row
    with open(sys.argv[1], "r") as content:
        puzzle = content.readlines()

    puzzle = [line.replace('\n', '') for line in puzzle]#removing newline

    #spliting the row string into lists of int to make 2d  9x9 size array
    puzzle = [list(map(int, puzzle[i].split(" "))) for i in range(len(puzzle))]

    return puzzle

def printer(puzzle: list):
    ''' prints the puzzle in a readable format
    '''
    for line in puzzle:
        for number in line:
            print(number, end=' ')#prints each number
        print()

def possiable(y: int, x: int, n: int, puzzle: list):
    ''' checks if the given number n can fit in given x,y postion
    '''
    #checks if number is in the row
    for i in range(9):
        if puzzle[y][i] == n:
            return False

    #checks if number is the coloum
    for i in range(9):
        if puzzle[i][x] == n:
            return False

    #getting the square the number is in
    x_0 = (x//3)*3
    y_0 = (y//3)*3

    #checks if the number is in its 3x3 square
    for i in range(3):
        for j in range(3):
            if puzzle[i+y_0][j+x_0] == n:
                return False

    #if all checks fail return True
    return True

def finished(puzzle: list):
    ''' checks if the puzzle is finished
    '''
    #looks through each postion
    for y in range(9):
        for x in range(9):

            #checks if empty
            if puzzle[x][y] == 0:
                return False

    return True

def solve(puzzle: list):
    ''' solves the puzzle
        using backtracking
    '''

    #looks through each postion
    for y in range(9):
        for x in range(9):

            #checks if empty
            if puzzle[y][x] == 0:

                #checks 1st possiable number and places it if can
                for n in range(1, 10):
                    if possiable(y, x, n, puzzle):
                        puzzle[y][x] = n

                        #repeat
                        solve(puzzle)

                        #if not finished and needs to backtrack
                        if not finished(puzzle):
                            puzzle[y][x] = 0

                return puzzle

    return puzzle

if __name__ == '__main__':
    check_file()
    PUZZLE = parser()
    PUZZLE = solve(PUZZLE)
    printer(PUZZLE)
