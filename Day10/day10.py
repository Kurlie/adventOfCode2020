# Read Input data file and store in an array
dI = open("day10Input.txt", "r")

# array to store input data
data = []

# strip \n and append to data
for i in dI:
    # dealing with integers so lets make the values in data integers
    data.append(int(i.replace("\n", "")))

dI.close()
data.sort()
# print(data)


def joltMultiple(list):
    jolt1 = list[0]
    jolt3 = 1
    for i in range(len(list)-1):
        if list[i+1]-list[i] == 1:
            jolt1 += 1
        if list[i+1]-list[i] == 3:
            jolt3 += 1
    return jolt1 * jolt3


print("part 1:", joltMultiple(data))
