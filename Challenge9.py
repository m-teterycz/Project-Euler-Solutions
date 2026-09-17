def get_triplet():
    for a in range(1,999):
        for b in range(1,999):
            if b < a:
                continue
            c = (a**2 + b**2)**0.5
           
            if a + b + c == 1000:
                return [a,b,c]
           
nums = get_triplet()
answer = 1
for num in nums:
    answer *= num

print(answer)