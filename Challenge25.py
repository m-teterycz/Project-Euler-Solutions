last_num = 0
current_num = 1
i = 2

while True:
    new_num = current_num + last_num
    current_num, last_num = new_num, current_num
    if len(str(new_num)) == 1000:
        print(i)
        break
    i += 1
