a,b = int(input()),int(input())

def minimumKnightMoves(x: int, y: int):
    steps = [[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1]]
    seen = []
    
    data = [[0, [0,0]]]
    
    while data:
        moves, current = data.pop(0)
        
        if current[0] == x and current[1] == y: return moves
            
        for i in steps:
            nextstep = [current[0]+i[0], current[1]+i[1]]
            
            if not ((nextstep[0] >= -2 and x >= -2
                        and nextstep[1] >= -2 and y >= -2) or
                        
                       (nextstep[0] <= 2 and x <= 2
                        and nextstep[1] <= 2 and y <= 2) or
                        
                       (nextstep[0] >= -2 and x >= -2
                        and nextstep[1] <= 2 and y <= 2) or
                        
                       (nextstep[0] <= 2 and x <= 2
                        and nextstep[1] >= -2 and y >= -2)):
                    continue
        
            if nextstep not in seen:
                data.append([moves+1, nextstep])
                seen.append(nextstep)
    
print(minimumKnightMoves(a,b))