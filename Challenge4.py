largest_palindrome = 0

def check_palindrome(num):
    if str(num)[::-1] == str(num):
        return True
    return False

for i in range(100, 1000):
    for j in range(i + 1, 1000):
        num = i * j
        if check_palindrome(num) and num > largest_palindrome:
            print(num)
            largest_palindrome = num
