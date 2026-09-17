def get_triangular_number(n):
    return (n*(n+1))//2

def check_divisors(num):
    divisors = 0
    limit = int(num ** 0.5)
    for i in range(1, limit + 1):
        if num % i == 0:
            divisors += 2 # counts i and num / i

        if limit * limit == num:
            divisors -= 1

    return divisors

num = 0
while True:
    num += 1
    triangular_number = get_triangular_number(num)
    if check_divisors(triangular_number) > 500:
        print(triangular_number)
        break