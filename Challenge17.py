def num_to_text(nums):
    text = ""
    n_to_t = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}
    suffix = {3:"Hundred", 2:"", 1:""}
    for i,num in enumerate(str(nums)):
        nums = str(nums)
        column = len(str(nums)) - i

        if column == 4: # thousands
            return "onethousand"

        elif column == 3: # hundreds
            text += f"{n_to_t[int(nums[i])]}{suffix[column]}"
            if int(nums[i + 1:]) != 0:
                text += "and"

        elif column == 2: # tens
            added_num = int(nums[i]) * 10 + int(nums[i + 1])
            
            if added_num in n_to_t and added_num <= 19:
                total_text = n_to_t[int(nums[i]) * 10 + int(nums[i + 1])]
                text += str(total_text)
                break

            else:
                text += n_to_t[int(nums[i]) * 10]

        elif column == 1: # ones
            text += f"{n_to_t[int(num)]}"

    return text

def count_letters(nums):
    result = ""
    for num in nums:
        if num != " ":
            result += num

    return len(result)


total_letters = 0
for i in range(1, 1001):
    text = num_to_text(i)
    total_letters += len(text)
    print(text)

print(total_letters)
