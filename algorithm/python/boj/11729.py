def hanoi(n, start, end):
    if n == 1 :
        print(start, end)
        return
       
    hanoi(n-1, start, 6-start-end) # 1, 2, 3중 start와 end를 제외한 나머지 곳이 end
    print(start, end)
    hanoi(n-1, 6-start-end, end) # 1, 2, 3중 start와 end를 제외한 나머지 곳이 start
    
n = int(input())
print(2**n-1)
hanoi(n, 1, 3)