nums = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

def format_nums(nums):
    nums = nums.split("\n")
    for i,num in enumerate(nums):
        nums[i] = num.split(" ")
   
    return nums

def search(parent_r, parent_c, total):
    largest = 0
    total += int(nums[parent_r][parent_c])
    rows = 14
    current_r = parent_r + 1
    max_col = current_r
       
       
    if parent_r == rows:
        return total
    if parent_c + 1 <= max_col: # go right
        result1 = search(current_r, parent_c + 1, total)
    result2 = search(current_r, parent_c, total) #go left
    
    return max(result1,result2)
   
nums = format_nums(nums)
print(search(0,0,0))


"""
Using recursion i can check the largest possible value from the left and right side.
Then i take the max value of each then return this which must be the largest sum.
For the 100 rows problem calculating all paths from nothing is slow.
Maybe use a dict to map an index to the value of the sum
"""