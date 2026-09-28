def factorial(num):
    total = num
    for i in range(1, num):
        total *= num - i
    return total


total = 0
num = 100
for char in str(factorial(num)):
    total += int(char)

print(total)