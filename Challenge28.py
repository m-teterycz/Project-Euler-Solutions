total = 1
step = 0
current_number = 1

for i in range(500):
    step += 2
    for i in range(4):
        current_number += step
        total += current_number

print(total)