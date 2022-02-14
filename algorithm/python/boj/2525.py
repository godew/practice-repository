h, m = map(int, input().split())
c = int(input())
res = (h * 60 + m + c) % 1440
print(res // 60, res % 60)