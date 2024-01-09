nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]
print(list(map(lambda x, y: (x + y, x - y), nums1, nums2)))
