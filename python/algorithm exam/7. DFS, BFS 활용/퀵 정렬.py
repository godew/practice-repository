# 퀵 정렬 
# 0. 분할과 정복, 전위 순회
# 1. 기준이 되는 pivot값 정하고 pivot을 기준으로 두 부분으로 나눈다.
# 2. 나뉜 두 부분에 대해 1번 과정을 진행한다.
# 3. 1,2 과정을 계속 반복하면 정렬이 완료 된다.

def Qsort(lt, rt):
    if lt < rt:
        pivot = arr[rt]
        pos = lt # pos : pivot보다 큰 값들의 집합중 제일 처음 인덱스
        for i in range(lt, rt):
            if arr[i] <= pivot:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1
                
        arr[rt], arr[pos] = arr[pos], arr[rt] # pos랑 pivot위치를 바꿔서 두 부분으로 나눔
        Qsort(lt, pos-1)
        Qsort(pos+1, rt)


if __name__ == "__main__":
    arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
    print("Before sort: ", arr)
    Qsort(0, 9)
    print()
    print("After sort: ", arr)


