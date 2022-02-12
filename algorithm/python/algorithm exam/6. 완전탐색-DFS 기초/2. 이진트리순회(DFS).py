import sys
import os

# os.chdir("C:\\python_study\\algorithm exam")
# sys.stdin = open("input.txt", "r")


def Pre_DFS(x, tree):
    if x > len(tree)-1:
        return
    print(tree[x], end=" ")
    Pre_DFS(2*x+1, tree)
    Pre_DFS(2*x+2, tree)

def In_DFS(x, tree):
    if x > len(tree)-1:
        return
    In_DFS(2*x+1, tree)
    print(tree[x], end=" ")
    In_DFS(2*x+2, tree)

def Post_DFS(x, tree):
    if x > len(tree)-1:
        return
    Post_DFS(2*x+1, tree)
    Post_DFS(2*x+2, tree)
    print(tree[x], end=" ")

def main():
    # tree = [1,2,3,4,5,6,7]
    tree = [23,5,6,1,2,45,4,11,3,7]

    Pre_DFS(0, tree); print()
    In_DFS(0, tree); print()
    Post_DFS(0, tree)

if __name__ == "__main__":
    main()

