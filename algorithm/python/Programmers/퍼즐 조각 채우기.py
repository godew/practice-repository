import copy
def rotate_90(table):
    tmp = [[0] * len(table) for _ in range(len(table))]
    for i in range(len(table)):
        for j in range(len(table)):
            tmp[j][len(table)-1-i] = table[i][j]

    return tmp

def DFS1(game_board, i, j, res): # game_board용 DFS
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    game_board[i][j] = 1
    for k in range(4):
        if 0 <= i + dx[k] <= len(game_board)-1 and 0 <= j + dy[k] <= len(game_board)-1:
            if game_board[i + dx[k]][j + dy[k]] == 0:
                res = DFS1(game_board, i + dx[k], j + dy[k], res + str(k))
    
    return res + ","

def DFS2(table, i, j, res): # table용 DFS
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    table[i][j] = 2
    for k in range(4):
        if 0 <= i + dx[k] <= len(table)-1 and 0 <= j + dy[k] <= len(table)-1:
            if table[i + dx[k]][j + dy[k]] == 1:
                res = DFS2(table, i + dx[k], j + dy[k], res + str(k))
    
    return res + ","

def DFS3(table, i, j): # table update용 DFS
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    table[i][j] = 0
    for k in range(4):
        if 0 <= i + dx[k] <= len(table)-1 and 0 <= j + dy[k] <= len(table)-1:
            if table[i + dx[k]][j + dy[k]] == 2:
                DFS3(table, i + dx[k], j + dy[k])

def isValid(table, tmp):
    for _ in range(4):
        table_copy = copy.deepcopy(table)

        for i in range(len(table)):
            for j in range(len(table)):
                if table_copy[i][j] == 1 and DFS2(table_copy, i, j, "") == tmp:
                    DFS3(table_copy, i, j)
                    # table에 2가있으면 전부 1로 변경
                    for i in range(len(table_copy)):
                        for j in range(len(table_copy)):
                            if table_copy[i][j] == 2:
                                table_copy[i][j] = 1
                    return [True, table_copy]

        table = rotate_90(table)

    return [False, table]


def solution(game_board, table):
    res = 0
    for i in range(len(table)):
        for j in range(len(table)):
            if game_board[i][j] == 0:
                tmp = DFS1(game_board, i, j, "")
                valid = isValid(table, tmp)
                table = valid[1]
                if valid[0]:
                    tmp = tmp.replace(",", "")
                    res += len(tmp)+1
    return res           

print(solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]]))