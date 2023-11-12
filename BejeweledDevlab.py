dimension = [int(i) for i in str(input()).split(" ")]
amount = dimension[0]*dimension[1]
real_vertical = dimension[0]-1
real_horizontal = dimension[1]-1
board = []

amount_list = [str(i) for i in range(1,amount+1)]
while len(amount_list) > 0:
    temp = amount_list[0:dimension[1]]
    board.append(temp)
    amount_list = amount_list[dimension[1]::]


def flaming(vertical: int, horizontal: int):    
    if vertical == 0:
        if horizontal == 0:
            board[0][0] = "0"
            board[0][1] = "0"
            board[0][2] = "0"
            board[1][0] = "0"
            board[1][1] = "0"
            board[1][2] = "0"
            board[2][0] = "0"
            board[2][1] = "0"
            board[2][2] = "0"
        elif horizontal == real_horizontal:
            board[0][real_horizontal] = "0"
            board[0][real_horizontal-1] = "0"
            board[0][real_horizontal-2] = "0"
            board[1][real_horizontal] = "0"
            board[1][real_horizontal-1] = "0"
            board[1][real_horizontal-2] = "0"
            board[2][real_horizontal] = "0"
            board[2][real_horizontal-1] = "0"
            board[2][real_horizontal-2] = "0"
        else:
            board[0][horizontal] = "0"
            board[0][horizontal+1] = "0"
            board[0][horizontal-1] = "0"
            board[1][horizontal] = "0"
            board[1][horizontal+1] = "0"
            board[1][horizontal-1] = "0"
            board[2][horizontal] = "0"
            board[2][horizontal+1] = "0"
            board[2][horizontal-1] = "0"
    elif vertical == real_vertical:
        if horizontal == 0:
            board[vertical][0] = "0"
            board[vertical][1] = "0"
            board[vertical][2] = "0"
            board[vertical-1][0] = "0"
            board[vertical-1][1] = "0"
            board[vertical-1][2] = "0"
            board[vertical-2][0] = "0"
            board[vertical-2][1] = "0"
            board[vertical-2][2] = "0"
        elif horizontal == real_horizontal:
            board[vertical][horizontal] = "0"
            board[vertical][horizontal-1] = "0"
            board[vertical][horizontal-2] = "0"
            board[vertical-1][horizontal] = "0"
            board[vertical-1][horizontal-1] = "0"
            board[vertical-1][horizontal-2] = "0"
            board[vertical-2][horizontal] = "0"
            board[vertical-2][horizontal-1] = "0"
            board[vertical-2][horizontal-2] = "0"
        else:
            board[vertical][horizontal] = "0"
            board[vertical][horizontal+1] = "0"
            board[vertical][horizontal-1] = "0"
            board[vertical-1][horizontal] = "0"
            board[vertical-1][horizontal+1] = "0"
            board[vertical-1][horizontal-1] = "0"
            board[vertical-2][horizontal] = "0"
            board[vertical-2][horizontal+1] = "0"
            board[vertical-2][horizontal-1] = "0"
    elif horizontal == 0:
        board[vertical][0] = "0"
        board[vertical][1] = "0"
        board[vertical][2] = "0"
        board[vertical-1][0] = "0"
        board[vertical-1][1] = "0"
        board[vertical-1][2] = "0"
        board[vertical+1][0] = "0"
        board[vertical+1][1] = "0"
        board[vertical+1][2] = "0"        
    elif horizontal == real_horizontal:
        board[vertical][horizontal] = "0"
        board[vertical][horizontal-1] = "0"
        board[vertical][horizontal-2] = "0"
        board[vertical-1][horizontal] = "0"
        board[vertical-1][horizontal-1] = "0"
        board[vertical-1][horizontal-2] = "0"         
        board[vertical+1][horizontal] = "0"
        board[vertical+1][horizontal-1] = "0"
        board[vertical+1][horizontal-2] = "0"  
    else:  
        board[vertical][horizontal] = "0"
        board[vertical][horizontal-1] = "0"
        board[vertical][horizontal+1] = "0"
        board[vertical+1][horizontal] = "0"
        board[vertical+1][horizontal-1] = "0"
        board[vertical+1][horizontal+1] = "0"       
        board[vertical-1][horizontal] = "0"
        board[vertical-1][horizontal-1] = "0"
        board[vertical-1][horizontal+1] = "0"        
        
    for z in range(0,3):
        for i in range(len(board)-1,-1,-1):
            for j in range(len(board[i])-1,-1,-1):
                if i != 0:
                    if board[i][j] == "0":
                        if board[i-1][j] != "0":
                            board[i][j] = str(board[i-1][j])
                            board[i-1][j] = "0"
            
def lightning(vertical: int, horizontal: int):
    for i in range(real_horizontal+1):
        board[vertical][i] = "0"
    for i in range(real_vertical+1):
        board[i][horizontal] = "0"

    for i in range(len(board)-1,-1,-1):
        for j in range(len(board[i])-1,-1,-1):
            if i != 0:
                if board[i][j] == "0":
                    if board[i-1][j] != "0":
                        board[i][j] = str(board[i-1][j])
                        board[i-1][j] = "0"

while True:
    target = [int(i) for i in str(input()).split(" ")]
    
    if target == [-1]: break
    
    while True:
        diamond_type = str(input()).lower() 
        if diamond_type == "f" or diamond_type == "l":
            if diamond_type == "f": flaming(target[0], target[1])
            if diamond_type == "l": lightning(target[0], target[1])
            break
        

displayboard = []
for i in board:
    temp = []
    for j in range(0,len(i)):
        if len(i[j]) == 1: temp.append(f" {i[j]}")
        else: temp.append(f"{i[j]}")
    displayboard.append(temp)
      
finalboard = []
Bigmode = False
BigBoard = False
for i in displayboard: 
    if int(displayboard[-1][0]) >= 10: Bigmode = True
    lines = ''
    for char in i:
        lines += char
        lines += "  "
    finalboard.append(lines)

if Bigmode: 
    for i in finalboard: print(f" {i}")
else:
    for i in finalboard: print(f"{i}")