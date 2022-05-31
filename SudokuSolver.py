import sys
import re

#check if file in command argumment is correct and is a txt file
def Check_file():
    if len(sys.argv) != 2 or re.search(".txt$",sys.argv[1]) is None:#if correct command length and is txt file
        print("please provide the text file with the Sudoku puzzle")
        quit()
    else:
        Parser()

#parses the input txt puzzle file
def Parser():
    with open(sys.argv[1],"r") as puzzle:
        contents = puzzle.read()

    print(contents)





if __name__ == '__main__':
    Check_file()
