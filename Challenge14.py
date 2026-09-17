def get_next_number(num):
    if num % 2 == 0:
        return num//2
    else:
        return 3*num + 1

seen = {}
i = 1
while len(seen) < 1000000:
    current_num = i
    terms = 0
    while current_num != 1:
        current_num = get_next_number(current_num)
        terms += 1

    terms += 1 # include the num 1
    seen[i] = terms
    i += 1 # go to the next starting point

print(seen)
for key in seen.keys():
    if seen[key] == 525:
        print(key)
