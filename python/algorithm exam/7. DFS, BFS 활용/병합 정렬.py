# 병합 정렬
# 1. 중앙을 기준으로 두 부분으로 계속 나눈다.
# 2. 나뉜 두 부분을 정렬한다.
# 3. 정렬된 두 부분을 합친다 -> 정렬된 두 부분을 앞에서부터 비교해나가면서 정렬해간다.

def Dsort(lt, rt):
    if lt < rt:
        mid = (lt+rt) // 2
        Dsort(lt, mid)
        Dsort(mid+1, rt)
        p1 = lt
        p2 = mid+1
        tmp = []
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1
            else:
                tmp.append(arr[p2])
                p2 += 1
        if p1 <= mid:
            tmp += arr[p1:mid+1]
        else:
            tmp += arr[p2:rt+1]
        for i in range(lt, rt+1):
            arr[i] = tmp[i-lt]


if __name__ == "__main__":
    arr = [23, 11, 45, 36, 15, 67, 33, 21]
    print("Before sort: ", arr)
    Dsort(0, 7)
    print()
    print("After sort: ", arr)