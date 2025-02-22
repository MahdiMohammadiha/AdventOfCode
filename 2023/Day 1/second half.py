"""
    Note:
        You may need to modify the configuration section
        to match your file paths, inputs, or environment.
"""

# configurations
FILE_NAME = "input.txt"

# read file
raw_datalist = open(FILE_NAME, "r")

# convert each line to list item
datalist = []
for raw_data in raw_datalist.readlines():
    datalist.append(raw_data.replace("\n", ""))


# convert letter form of numbers to digit ones
def convert_letter_to_digits(arg):
    return (
        arg.replace("oneight", "18")
        .replace("twone", "21")
        .replace("threeight", "38")
        .replace("fiveight", "58")
        .replace("sevenine", "79")
        .replace("eightwo", "82")
        .replace("eighthree", "83")
        .replace("nineight", "98")
        .replace("one", "1")
        .replace("two", "2")
        .replace("three", "3")
        .replace("four", "4")
        .replace("five", "5")
        .replace("six", "6")
        .replace("seven", "7")
        .replace("eight", "8")
        .replace("nine", "9")
    )


# backwars the given word
def reverse_word(arg):
    return arg[::-1]


# returns the first number in the given word
def get_first_number(arg):
    for letter in arg:
        if letter.isnumeric():
            return letter
    raise Exception("No number found!")


sum = 0
for data in datalist:
    # convert letter to digits
    data = convert_letter_to_digits(data)

    # get first number
    first_number = get_first_number(data)

    # get last number
    data = reverse_word(data)
    last_number = get_first_number(data)

    # pair the numbers
    number = first_number + last_number

    sum += int(number)

print(sum)
