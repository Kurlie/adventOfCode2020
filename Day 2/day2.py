# Read Input data file and store in an array
dI = open("day2Input.txt", "r")

# array to store input data
data = []

# strip \n and append to data
for i in dI:
    #value = i.strip()
    value = i.split()
    data.append(value)

dI.close()

# print(data)

####--------------------------------------------------------------------------------#####
####--------------------------------------------------------------------------------#####

# part 1:
valid = 0

for j in data:
    arr = j[0].split('-')
    count = j[2].count(j[1][0])

    if (count >= int(arr[0]) and count <= int(arr[1])):
        valid += 1

    #print(arr, j[1], j[2], count, valid)

print(valid)

####--------------------------------------------------------------------------------#####
####--------------------------------------------------------------------------------#####

# part 2:
valid2 = 0

for t in data:
    arr2 = t[0].split('-')

    if (t[2][int(arr2[0])-1] == t[1][0] and t[2][int(arr2[1])-1] != t[1][0]):
        valid2 += 1
    elif (t[2][int(arr2[0])-1] != t[1][0] and t[2][int(arr2[1])-1] == t[1][0]):
        valid2 += 1

    #print(arr2, t[1], t[2], valid2)

print(valid2)
