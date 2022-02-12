import bisect
nums = [3,1]; target = 3

lt = 0
rt = len(nums)-1

while True:
    mid = (lt+rt)//2
    if mid == 0:
        if len(nums) == 1:
            idx = mid
        else:
            if nums[0] < nums[1]:
                idx = mid
            else:
                idx = mid + 1
        break
    if nums[mid] < nums[mid-1]:
        idx = mid # 무조건 존재
        break
    if nums[mid] < nums[rt]:
        rt = mid - 1
    elif nums[mid] > nums[rt]:
        lt = mid + 1

nums = nums[idx:] + nums[:idx]

res = bisect.bisect_left(nums, target)

if res < len(nums) and nums[res] == target:
    if res + idx >= len(nums):
        print(res + idx - len(nums))
    else:
        print(res + idx)
else:
    print(-1)




# try:
#     return nums.index(target)
# except ValueError:
#     return -1