import sys
import os

# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0; rt = n-1
while True:
    mid = (rt+lt)//2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1

# 재귀 함수 표현
def binarySearch(array, value, low, high):
	if low > high:
		return False
	mid = (low+high) // 2
	if array[mid] > value:
		return binarySearch(array, value, low, mid-1)
	elif array[mid] < value:
		return binarySearch(array, value, mid+1, high)
	else:
		return mid