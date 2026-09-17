def check_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_prime_factor(num):
    if check_prime(num):
        return num
    for i in range(2, num):
        if num % i == 0 and check_prime(num // i):
            return num // i

    return None

num = 600851475143
prime_factors = []
factorised = False

while factorised == False:
    prime_factor = get_prime_factor(num)
    if prime_factor == None:
        break
    prime_factors.append(prime_factor)
    num = num // prime_factor

print(max(prime_factors))
