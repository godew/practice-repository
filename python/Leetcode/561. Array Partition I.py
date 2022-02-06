nums = [1,4,3,2]
nums.sort()
tot = 0
for i in range(0, len(nums), 2):
    tot += nums[i]

print(tot)