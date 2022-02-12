import sys
import os
# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")


num = int(input())
List = list(map(int, input().split()))
# total = 0
# for i in List:
#     total += i

# if total/num - total//num >= 0.5:
#     avg = total//num + 1
# else:
#     avg = total//num

avg =int(sum(List)/num + 0.5)# 9~16 line을 한번에 해결
List_min = float("inf")
for i in range(len(List)):
    if List_min >= abs(avg-List[i]):
        if List_min == abs(avg-List[i]):
            if List[idx] >= List[i]:
                List_min = abs(avg-List[idx])
                continue
            else:
                 List_min = abs(avg-List[i])
                 idx = i
                 continue
        List_min = abs(avg-List[i])
        idx = i
print(avg, idx+1)

# 해답코드
# for idx, x in enumerate(a):
#     tmp=abs(x-ave)
#     if tmp<min:
#         min=tmp
#         score=x
#         res=idx+1
#     elif tmp==min:
#         if x>score:
#             score=x
#             res=idx+1
        

