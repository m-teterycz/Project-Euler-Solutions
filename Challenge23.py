import math

def get_proper_divisors(num):
    total = 1
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            other_pair = num // i
            if other_pair == i:
                total += i
            else:
                total += other_pair + i
    return total

def check_type(num):
    if num in abundant_nums:
        return "A"
    if num in non_abundant_nums:
        return None

    
    result = get_proper_divisors(num)
    if result > num:
        abundant_nums.add(num)
        return "A"
    else:
        non_abundant_nums.add(num)

def get_add_factors(num):
    for i in range(1, num // 2 + 1):
        other_num = num - i
        if check_type(other_num) == "A" and check_type(i) == "A":
            return True


non_abundant_nums = set()
abundant_nums = set()
total = 0
for i in range(1, 28124):
    if not get_add_factors(i):
        total += i
       
print(total)




"""
IMPROVEMENTS MADE FOR EFFICIENCY:
    When repeating alot of the same calculation store the result in a set instead of calculating it everytime thousands of times
    When getting pairs of values e.g added factors or normal factors you can just calculate the other pair from the origianl halfing the amount of loops
    Try to do the minimum amount of steps to reach a certain format. Making a plan is good for this.
"""