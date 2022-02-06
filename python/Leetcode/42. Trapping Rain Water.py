# height = [4,2,0,3,2,5]

# lt = rt = 0
# res = 0
# while lt < len(height)-1:
#     rt += 1
#     if height[rt] >= height[lt]:
#         tmp = height[lt]
#         lt += 1
#         while lt < rt:
#             res += tmp - height[lt]
#             lt += 1
    
#     if rt == len(height)-1:
#         if lt == len(height)-1:
#             break
#         h = max(height[lt+1:])
#         lt += 1
#         while height[lt] != h:
#             res += h - height[lt]
#             lt += 1
#         rt = lt

# print(res)
    

# # 해답 코드

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0

#         volume = 0
#         left, right = 0, len(height) - 1
#         left_max, right_max = height[left], height[right]

#         while left < right:
#             left_max, right_max = max(height[left], left_max), max(height[right], right_max)
#             # 더 높은 쪽을 향해 투 포인터 이동
#             if left_max <= right_max:
#                 volume += left_max - height[left]
#                 left += 1
#             else:
#                 volume += right_max - height[right]
#                 right -= 1
#         return volume


    