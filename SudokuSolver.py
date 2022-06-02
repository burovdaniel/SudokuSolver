import sys
import re

#check if file in command argumment is correct and is a txt file
def Check_file():
    if len(sys.argv) != 2 or re.search(".txt$",sys.argv[1]) is None:#if correct command length and is txt file
        print("please provide the text file with the Sudoku puzzle")
        quit()
    else:
        pass

#parses the input txt puzzle file into a 2d int 9x9 array
#dosent check if input is correct(two same numbers in a line etc) currently
def Parser():
    #opens the input puzzle and saves as list of the string row
    with open(sys.argv[1],"r") as content:
        puzzle = content.readlines()

    puzzle = [line.replace('\n','') for line in puzzle]#removing newline

    #spliting the row string into lists of int to make 2d  9x9 size array
    puzzle = [list(map(int,puzzle[i].split(" "))) for i in range(len(puzzle))]

    return puzzle

#Prints the puzzle in a readable format
def Printer(puzzle : list):

    for line in puzzle:
        for number in line:
            print(number,end=' ')#prints each number
        print()#newline

#Checks if the n number can be placed in xy postion
def Possiable(y:int,x:int,n:int,puzzle:list):
    #checks if number is in the row
    for i in range(9):
        if(puzzle[y][i] == n):
            return False

    #checks if number is the coloum
    for i in range(9):
        if(puzzle[i][x] == n):
            return False

    #getting the square the number is in
    x0 = (x//3)*3
    y0 = (y//3)*3

    #checks if the number is in its 3x3 square
    for i in range(3):
        for j in range(3):
            if(puzzle[i+y0][j+x0] == n):
                return False

    #if all checks fail return True
    return True

if __name__ == '__main__':
    #puzzle[y][x]
    Check_file()
    puzzle = Parser()
    #Printer(puzzle)
    print(Possiable(0,0,4,puzzle))

