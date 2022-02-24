import sys
from collections import Counter

n = int(input())
tmp = []
for _ in range(n):
    tmp.append(int(sys.stdin.readline()))

tmp.sort()
# 산술평균
print(round(sum(tmp) / n))

# 중앙값
print(tmp[n // 2])

# 최빈값
ct = Counter(tmp).most_common()
repo = ct[0][1]
for i in range(1, len(ct)):
    if repo != ct[i][1]:
        print(sorted(ct[:i], key= lambda x : x[0])[1][0])
        break


# 범위
print(tmp[-1] - tmp[0])
