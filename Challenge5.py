def check_evenly_divisible(num):
    for i in range(1, 20):
        if num % i == 0:
            pass
        else:
            return False
    return True

num = 1
while True:
    if check_evenly_divisible(num):
        break
    num += 1


print(num)