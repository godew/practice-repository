def solution(m, n, board):
    for idx, s in enumerate(board):
        board[idx] = list(s)
        
    ch = list([0]*n for _ in range(m))
    res = 0
    while True:
        cnt = 0
        for x in range(m):
            for y in range(n):
                if board[x][y] == None:
                    continue
                # 블럭이 지워지는 4가지 경우
                if 0<= x-1 <=m-1 and 0<= y-1 <=n-1:
                    if board[x][y] == board[x-1][y] and board[x][y] == board[x][y-1] and board[x][y] == board[x-1][y-1]:
                        ch[x][y] = 1
                        cnt += 1
                        continue

                if 0<= x-1 <=m-1 and 0<= y+1 <=n-1:                   
                    if board[x][y] == board[x-1][y] and board[x][y] == board[x][y+1] and board[x][y] == board[x-1][y+1]:
                        ch[x][y] = 1
                        cnt += 1
                        continue

                if 0<= x+1 <=m-1 and 0<= y+1 <=n-1:
                    if board[x][y] == board[x+1][y] and board[x][y] == board[x][y+1] and board[x][y] == board[x+1][y+1]:
                        ch[x][y] = 1
                        cnt += 1
                        continue

                if 0<= x+1 <=m-1 and 0<= y-1 <=n-1:
                    if board[x][y] == board[x+1][y] and board[x][y] == board[x][y-1] and board[x][y] == board[x+1][y-1]:
                        ch[x][y] = 1
                        cnt += 1
                        continue
        if cnt == 0:
            break
        else:
            res += cnt
        
        # 블럭이 아래로 떨어짐
        for x in range(m):
            for y in range(n):
                if ch[x][y] == 1:
                    if x == 0:
                        board[0][y] = None
                        continue
                    ch[x][y] = 0
                    for i in range(x, 0, -1):
                        board[i][y] = board[i-1][y]
                    board[0][y] = None

    return res

    
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))

