numbers = [2,7,11,15]; target = 9
lt = 0
rt = len(numbers)-1

while True:
    if numbers[lt] + numbers[rt] > target:
        rt -= 1
    elif numbers[lt] + numbers[rt] < target:
        lt += 1
    else:
        print([lt+1, rt+1])
        break