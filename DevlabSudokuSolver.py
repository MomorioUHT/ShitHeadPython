original = []
board = []

for i in range(9):
    temp = str(input())
    board.append([str(i) for i in temp])
    original.append([str(i) for i in temp])
    
def possiblePlace(y,x,n):
    for i in range(9):
        if str(board[y][i]) == n: return False
        elif str(board[i][x]) == n: return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if str(board[y0+i][x0+j]) == n: return False
    return True

def solve(board):
    for y in range(9):
        for x in range(9):
            if board[y][x] == "0":
                for n in range(1,10):
                    if possiblePlace(y,x,str(n)):
                        board[y][x] = str(n)
                        if solve(board): return True
                        board[y][x] = "0"
                return False
    return True
solve(board)

def printthisshitout(gameboard: list):
    countlines = 0
    for context in gameboard:
        final = ''
        final += "  "
        if countlines == 3 or countlines == 6: print(" ")
        for i in range(len(context)):
            if context[i] == "0": final += "0"
            else: final += str(context[i])
            if i == 2 or i == 5: final += "   "
            else: final += "  "
        print(final)
        countlines += 1

print(" ")
printthisshitout(original)
print(" ")
print("-------------------------------")
print(" ")
printthisshitout(board)