import sys
import os

os.chdir("C:\\python_study\\algorithm exam")
sys.stdin = open("input.txt", "r")

def BFS(x):
    if x > 0:
        return BFS(x//2) + str(x%2)
    return ""

def main():
    n = int(input())
    print(BFS(n))

if __name__ == "__main__":
    main()

