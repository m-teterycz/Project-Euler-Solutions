def get_proper_divisors(num):
    total = 0
    for i in range(1,num):
        if num % i == 0:
            total += i
   
    return total
           

ami_nums = []
for i in range(1,10001):
    divided_sum = get_proper_divisors(i)
    if get_proper_divisors(divided_sum) == i and divided_sum != i:
        ami_nums.append(i)

total = 0
for num in ami_nums:
    total += num
print(total)