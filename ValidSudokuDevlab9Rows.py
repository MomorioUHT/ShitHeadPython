board = []
for i in range(9):
    x = [i for i in str(input())]
    board.append(x)
final = []

def duplicateCheck(x: list):
    res = []
    for i in x: 
        if i not in res: res.append(i)
    if len(res) != len(x): final.append("False")
    else: final.append("True")

for i in range(9):
    row = []
    col = []
    for j in range(9):
        if i%3 == 0 and j%3 == 0:
            array = []
            for a in range(i,i+3):
                for b in range(j,j+3):
                    if board[a][b] != '0':
                        array.append(board[a][b])
            duplicateCheck(array)
        
for i in range(9):
    row = []
    col = []
    for j in range(9):
        if board[i][j] != '0': row.append(board[i][j])
        if board[j][i] != '0': col.append(board[j][i])
    duplicateCheck(row)
    duplicateCheck(col)

if "False" in final: print("False")
else: print("True")