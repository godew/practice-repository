nums = [-1,0,1,2,-1,-4]
nums.sort()
res = []

for i in range(len(nums)-2):
    if i > 0 and nums[i] == nums[i-1]:
        continue

    lt = i+1
    rt = len(nums)-1
    
    while lt < rt:
        tot = nums[i] + nums[lt] + nums[rt]

        if tot > 0:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
            rt -= 1
        elif tot < 0:
            lt += 1
        else:
            res.append([nums[i], nums[lt], nums[rt]])
            while lt < rt  and nums[lt+1] == nums[lt]:
                lt += 1
            while lt < rt  and nums[rt-1] == nums[rt]:
                rt -= 1
            lt += 1
            rt -= 1

print(res)