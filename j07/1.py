nums = input().split()
nums = [int(i) for i in nums]

# sums, lenght, max_num, min_num = 0, 0, nums[0], nums[0]

# for _ in nums:
#     if 0 <= _ <= 20:
#         sums += _
#         lenght += 1
#         if _ > max_num:
#             max_num = _
#         if min_num < 0:
#             min_num = nums[1]
#         if _ < min_num and min_num >= 0:
#             min_num = _
#     else:
#         continue

# print(f"sum: {sums}\naverage: {sums/lenght}\nmax: {max_num}\nmin: {min_num}")

print(f"avg : {sum(nums)/len(nums)}\nmax: {max(nums)}\nmin: {min(nums)}")