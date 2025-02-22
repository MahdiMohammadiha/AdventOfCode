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
    point_flag = True

    for game_set in range(len(datalist[game_round])):
        set_sum = 0

        for game_pack in range(len(datalist[game_round][game_set])):

            # get the key and values of each pack
            cube_key = str(list(datalist[game_round][game_set][game_pack].keys())[0])
            cube_value = int(list(datalist[game_round][game_set][game_pack].values())[0])

            set_sum += cube_value
            if set_sum > RED_CUBES + GREEN_CUBES + BLUE_CUBES:
                point_flag = False
                break

            if cube_key == "red":
                if cube_value > RED_CUBES:
                    point_flag = False
                    break
            elif cube_key == "green":
                if cube_value > GREEN_CUBES:
                    point_flag = False
                    break
            elif cube_key == "blue":
                if cube_value > BLUE_CUBES:
                    point_flag = False
                    break
            else:
                raise Exception(
                    "Unknown cube name found!\n\tCube name: " + str(cube_key)
                )

    if point_flag:
        point_sum += game_round + 1

print(point_sum)
