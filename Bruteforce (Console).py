# Made without research, just using simple backtracking algorithm

# Dependencies
import timeit # For timing

# Initial board
board = [
    0, 2, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 6, 0, 0, 0, 0, 3,
    0, 7, 4, 0, 8, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 3, 0, 0, 2,
    0, 8, 0, 0, 4, 0, 0, 1, 0,
    6, 0, 0, 5, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 7, 8, 0,
    5, 0, 0, 0, 0, 9, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 4, 0
]

# Print the board in a readable format
def printBoard():
    print("-"*25)
    
    for i1 in range(0, 9):
        row = ""

        for i2 in range(i1*9, i1*9+9):
            row += str(board[i2])+", "

        print(row[:-2])
    
    print("-"*25)

# List position to X co-ordinate
# Returns integer (X co-ordinate)
def getX(pos):
    return pos%9

# List position to Y co-ordinate
# Returns integer (Y co-ordinate)
def getY(pos):
    return pos//9

# Co-ordinates to list position
# Returns integer (list position)
def getPos(x, y):
    return x + y*9

# Get top left list position of 3x3 square that supplied list position is in
# Returns integer (list position)
def getSquareTopLeft(pos):
    x = getX(pos)
    y = getY(pos)
    
    xTop = x-x%3
    yTop = y-y%3
    
    return getPos(xTop, yTop)

# Check if given value is valid to be used in list position
# Returns bool (valid state)
def isValid(val, pos):
    x = getX(pos)
    y = getY(pos)

    # Check row and column for duplicates
    for i in range(0, 9):
        testX = getPos(i, y)
        testY = getPos(x, i)

        if testX != x and board[testX] == val:
            return False
        elif testY != y and board[testY] == val:
            return False
    
    topLeft = getSquareTopLeft(pos)

    # Check 3x3 grid for duplicates
    for i1 in range(0, 3):
        for i2 in range(0, 3):
            testPos = topLeft + getPos(i1, i2)

            if testPos != pos and board[testPos] == val:
                return False
    
    return True

# Increases value on board in supplied list position until valid integer is found
# Returns integer (next valid number, or 0 if none are valid)
def getNextValid(pos):
    val = board[pos]

    for i in range(val+1, 10):
        if isValid(i, pos):
            return i

    return 0

# Gets next empty (0) square in board from supplied list position
# Returns integer (list position)
# Returns None (when no empty squares)
def getNextEmptyFrom(pos):
    for i in range(pos, len(board)):
        if board[i] == 0:
            return i

print("Solving...")

# Start timer
startTime = timeit.default_timer()

# Array of filled in list positions (for backtracking)
filled = []

# Set current to first empty square
current = getNextEmptyFrom(0)

# While there are still empty squares
while current != None:
    nextValid = getNextValid(current)
    board[current] = nextValid

    if nextValid != 0:
        filled.append(current)
        
        current = getNextEmptyFrom(current)
    else:
        if len(filled) > 0:
            current = filled.pop()
        else:
            print("Unsolvable board!")
            break

endTime = timeit.default_timer()

printBoard()
print(f"Took {endTime-startTime} seconds to complete")
