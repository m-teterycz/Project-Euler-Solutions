def check_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_next_prime(last_prime):
    current_number = last_prime + 1
    while True:
        if check_prime(current_number):
            return current_number
        current_number += 1


prime_count = 0
prime_number = 0

while True:
    if prime_count == 10001:
        print(prime_number)
        break

    prime_number = get_next_prime(prime_number)
    prime_count += 1