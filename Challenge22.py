letter_to_value = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
def text_to_num(name):
    total = 0
    for char in name:
        total += letter_to_value[char.lower()] # Couldve just made the dict in uppercase
    return total

path = "C:/Users/user/Downloads/0022_names.txt"
f = open(path, "r")
data = f.read().split(",")
data.sort()
for i,value in enumerate(data):
    data[i] = value.strip('"')


total_score = 0
for i in range(len(data)):
    total_score += text_to_num(data[i]) * (i + 1)

print(total_score)