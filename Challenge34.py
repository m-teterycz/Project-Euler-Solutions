def factorial(num):
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total

def check_curious(nums):
    total = 0
    for num in str(nums):
        total += factorial(int(num))

    if total == nums:
        return True
    return False


x = 1
while not(x * 362880 < 10**(x - 1)): # find the upper digit bound
    x += 1

i = 3
total = 0
while len(str(i)) < 8:
    if check_curious(i):
        total += i
    i += 1

print(total)
