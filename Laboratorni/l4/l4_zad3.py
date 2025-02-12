nums = list(i for i in range(1, 101) if i % 2 == 0 or i % 5 == 0)
nums.reverse()
print(nums)

chetni = list(i for i in nums if i % 2 == 0)
nechetni = list(i for i in nums if i % 2 != 0)

print(chetni, "\n", nechetni)