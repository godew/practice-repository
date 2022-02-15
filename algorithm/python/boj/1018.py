def count(chess):
    # 왼쪽 위가 B일 경우
    cntB = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0 and chess[i][j] == "W" or (i + j) % 2 != 0 and chess[i][j] == "B":
                    cntB += 1

    # 왼쪽 위가 W일 경우
    cntW = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0 and chess[i][j] == "B" or (i + j) % 2 != 0 and chess[i][j] == "W":
                    cntW += 1
    
    return min(cntB, cntW)

n, m = map(int, input().split())
board = [input() for _ in range(n)]
res = 2500
for i in range(n-7):
    for j in range(m-7):
        chess = [board[k][j:j+8] for k in range(i, i+8)]
        res = min(res, count(chess))

print(res)