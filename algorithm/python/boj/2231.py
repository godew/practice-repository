n = input()
l = len(n)
n = int(n)

for x in range(n - 9 * l, n):
    if x >= 1 and x + sum(map(int, list(str(x)))) == n:
        print(x)
        break
else:
    print(0)
