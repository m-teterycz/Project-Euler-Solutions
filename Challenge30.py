def calculate_value(nums):
    total = 0
    for num in str(nums):
        total += int(num)**5
    return total



valid = []
for i in range(9**5 * 4):
    if calculate_value(i) == i:
        valid.append(i)

total = 0
for num in valid:
    total += num

print(total - 1)