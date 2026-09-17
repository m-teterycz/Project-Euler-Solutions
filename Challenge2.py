fibonacci = [1,2]
i = 0
total = 2
while fibonacci[len(fibonacci) - 1] < 4000000:
    latest_num = fibonacci[i] + fibonacci[i + 1]
    fibonacci.append(latest_num)
    if latest_num % 2 == 0:
        total += latest_num

    i += 1

print(total)