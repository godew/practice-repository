nums = [2,7,11,15]
target = 9

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i]+nums[j] == target:
#             print([i, j])


# 해답 코드
nums_map = {}
for idx, x in enumerate(nums):
    nums_map[x] = idx

for idx, x in enumerate(nums):
    if target-x in nums_map and idx != nums_map[target-x]:
        print([idx, nums_map[target-x]])
