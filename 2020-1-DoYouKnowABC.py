input_list = input().split()
nums = list(map(int, input_list))

# step 1. sort the input list
nums.sort()

# step 2. find ABC
# index:  0  1    2           3     4     5     6
# num:    A  B   C or A+B     A+B   A+C   B+C   A+B+C
a = nums[0]
b = nums[1]
c = nums[4] - a

print(a, b, c)

