nums1 = [4,9,5]; nums2 = [9,4,9,8,4]

if len(nums1) > len(nums2):
    nums1, nums2 = nums2, nums1
    
res = []
for x in nums1:
    if x in nums2:
        res += [x]

print(res)