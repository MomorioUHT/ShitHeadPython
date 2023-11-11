context = str(input())
board = []
while len(context) > 0:
    board.append(context[0:9])
    context = context[9::]
for i in board: print(i)