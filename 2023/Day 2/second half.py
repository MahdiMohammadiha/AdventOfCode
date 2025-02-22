"""
    Note:
        You may need to modify the configuration section
        to match your file paths, inputs, or environment.
"""

# configurations
FILE_NAME = "input.txt"
RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

# read file
raw_data = open(FILE_NAME, "r")


# convert each pack in sets into dictionary
def rgb_digit_dict(arg):
    arg = arg.split(" ")
    return {arg[1]: arg[0]}


# convert games to list
datalist = []
raw_datalist = (raw_data.read()).replace("\n", "*").split("*")
for data in raw_datalist:
    data = data.split(": ")
    datalist.append(data[1])

# convert sets to list
for index in range(len(datalist)):
    data = datalist[index].split("; ")

    # convert packs to list
    for inner_index in range(len(data)):
        inner_data = data[inner_index].split(", ")

        # keep digits only
        for i in range(len(inner_data)):
            inner_data[i] = rgb_digit_dict(inner_data[i])

        data[inner_index] = inner_data

    datalist[index] = data

# add all games point
point_sum = 0

for game_round in range(len(datalist)):
    set_sum = 0
    high_red = 0
    high_green = 0
    high_blue = 0

    for game_set in range(len(datalist[game_round])):

        for game_pack in range(len(datalist[game_round][game_set])):

            # get the key and values of each pack
            cube_key = str(list(datalist[game_round][game_set][game_pack].keys())[0])
            cube_value = int(list(datalist[game_round][game_set][game_pack].values())[0])

            if cube_key == "red":
                if cube_value > high_red:
                    high_red = cube_value
            elif cube_key == "green":
                if cube_value > high_green:
                    high_green = cube_value
            elif cube_key == "blue":
                if cube_value > high_blue:
                    high_blue = cube_value
            else:
                raise Exception(
                    "Unknown cube name found!\n\tCube name: " + str(cube_key)
                )

    set_sum = high_red * high_green * high_blue
    point_sum += set_sum

print(point_sum)
