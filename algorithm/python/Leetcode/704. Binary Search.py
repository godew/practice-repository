nums = [-1,0,3,5,9,12]; target = 9

lt = 0
rt = len(nums)-1

while lt < rt:
    mid = (rt+lt) // 2
    if target == nums[mid]:
        print(mid)
        break
    elif target > nums[mid]:
        lt = mid+1
    else:
        rt = mid-1
else:
    print(-1)