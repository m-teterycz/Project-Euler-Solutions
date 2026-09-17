def factorial(num):
    result = 1
    for i in range(num, 1, -1):
        result *= i
    return result
   

grid_size = 20
top_term = factorial(grid_size * 2) // (factorial(grid_size) ** 2)
print(top_term)