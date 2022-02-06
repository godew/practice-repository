nums = [1,2,3,4]
l = len(nums)
lm = [1]*l
rm = [1]*l
res = []
for i in range(1, l):
    lm[i] = lm[i-1]*nums[i-1]
    rm[l-1-i] = rm[l-i]*nums[l-i]


for i in range(l):
    res.append(lm[i]*rm[i])

print(res)
