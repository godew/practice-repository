import turtle as t
import random as r
import time

dy = [-1,0,1,0]
dx = [0,1,0,-1]

class Brick():
    def __init__(self):
        self.y = 0
        self.x = 7
        self.color = r.randint(1,6)

    def left(self, grid): # 왼쪽으로 좌표이동
        if grid[self.y][self.x-1] == 0 and grid[self.y+1][self.x-1] == 0:
            grid[self.y][self.x] = 0
            self.x -= 1
    
    def right(self, grid): # 오른쪽으로 좌표이동
        if grid[self.y][self.x+1] == 0 and grid[self.y+1][self.x+1] == 0:
            grid[self.y][self.x] = 0
            self.x += 1

def DFS(y, x, grid, color):
    global ch, blank
    ch[y][x] = 1
    blank.append((y,x))
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if grid[yy][xx] == color and ch[yy][xx] == 0:
            DFS(yy, xx, grid, color)

def max_height(grid):
    for y in range(1, 24):
        for x in range(1, 13):
            if grid[y][x] != 0:
                return y

def grid_update(grid, blank):
    for y,x in blank:
        grid[y][x] = 0
    height = max_height(grid)
    for y in range(23,height,-1):
        for x in range(1,13):
            if grid[y][x] == 0:
                tmp_y = y
                while grid[tmp_y-1][x] == 0 and tmp_y-1 > 0:
                    tmp_y -= 1
                grid[y][x] = grid[tmp_y-1][x]
                grid[tmp_y-1][x] = 0

def continual_remove():
    global ch, blank
    while True:
        flag = 1
        for y in range(23, 15, -1):
            for x in range(1, 13):
                if grid[y][x] != 0:
                    ch = [[0]*14 for _ in range(25)]
                    blank = []
                    DFS(y, x, grid, grid[y][x])
                    if len(blank) >= 4:
                        grid_update(grid, blank)
                        flag = 0
                        
        draw_grid(block, grid)
        if flag == 1:
            break



def game_over():
    pen.up() # 펜을 들어야한다 아니면 옮기는게 그려진다.
    pen.goto(-120, 100)
    pen.write("GAME OVER", font=("courier", 30))

def win():
    pen.up()
    pen.goto(-95, 100)
    pen.write("YOU WIN", font=("courier", 30))

def draw_grid(block, grid):
    block.clear() # 버퍼 clear
    top = 250
    left = -150
    colors = ["black", "red", "blue", "orange", "yellow", "green", "purple", "white"]
    for y in range(len(grid)): # 행을 y
        for x in range(len(grid[0])): # 열을 x
            sc_x = left + x*22 # 격자 하나에 20픽셀이다.
            sc_y = top - y*22
            block.goto(sc_x, sc_y)
            if y == 15 and grid[y][x] == 7: # 이 줄이 넘어가면 game over
                block.color("red") # 줄을 red로 표시
            else:
                block.color(colors[grid[y][x]])
            block.stamp() # 스크린에 모양을 찍는다.


if __name__ == "__main__":
    sc = t.Screen()
    sc.tracer(False) # 그래픽을 빨리 그린다.
    sc.bgcolor("black")
    sc.setup(width=600, height=700)

    grid = [[0]*12 for _ in range(24)]
    for i in range(24):
        grid[i].insert(0, 7)
        grid[i].append(7)
    grid.append([7]*14)

    for y in range(21, 24): 
        for x in range(1,13):
            grid[y][x] = r.randint(1,6)

    block = t.Turtle()
    block.penup() # block이 이동하면서 그림을 안그린다.
    block.speed(0)
    block.shape("square")
    block.setundobuffer(None) # 버퍼를 undo 해서 안쌓이게한다.

    brick = Brick()
    grid[brick.y][brick.x] = brick.color
    draw_grid(block, grid)

    # 스크린에 글씨 쓰기.
    pen = t.Turtle()
    pen.ht() # hide turtle
    pen.goto(-85, 290)
    pen.color("white")
    pen.write("Block Game", font=("courier", 20))



    # 꾹누르면 계속 입력된다.
    sc.onkeypress(lambda : brick.left(grid), "Left")
    sc.onkeypress(lambda : brick.right(grid), "Right")
    sc.listen() # 키가 작동

    time.sleep(2)
    while True: # 블록을 아래로 내린다.
        sc.update()
        if grid[brick.y+1][brick.x] == 0:
            grid[brick.y][brick.x] = 0
            brick.y += 1
            grid[brick.y][brick.x] = brick.color
        else:
            ch = [[0]*14 for _ in range(25)]
            blank = []
            DFS(brick.y, brick.x, grid, brick.color)
            if len(blank) >= 4:
                grid_update(grid, blank)
                continual_remove()

            height = max_height(grid)
            if height <= 15:
                game_over()
                break

            elif height >= 22: 
                draw_grid(block, grid)
                win()
                break

            brick = Brick()

        draw_grid(block, grid)
        time.sleep(0.03)
    
    sc.mainloop() # 창이 계속 켜지게


