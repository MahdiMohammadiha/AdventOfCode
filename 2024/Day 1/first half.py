"""
    Note:
        You may need to modify the configuration section
        to match your file paths, inputs, or environment.
"""

# Configurations
FILE_NAME = "input.txt"

# Read file
with open(FILE_NAME, "r") as file:
    raw_data = file.read()

# Convert to list
raw_datalist = raw_data.replace("   ", "\n").split("\n")

# Divide elements into left and right list
def is_even(counter):
    return not counter % 2

left_list = []
right_list = []
cnt = 0

while cnt < len(raw_datalist):
    if is_even(cnt):
        left_list.append(raw_datalist[cnt])
    else:
        right_list.append(raw_datalist[cnt])
    cnt += 1

# Calculate the total difference
left_list.sort()
right_list.sort()
total_diff = 0

for left_ele, right_ele in zip(left_list, right_list):
    total_diff += abs(int(left_ele) - int(right_ele))

print(total_diff)
