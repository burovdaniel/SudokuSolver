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

if __name__ == '__main__':
    Check_file()
    puzzle = Parser()
    Printer(puzzle)
