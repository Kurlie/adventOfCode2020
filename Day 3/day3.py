# Read Input data file and store in an array
dI = open("day3Input.txt", "r")

# print(dI.read())

# array to store input data
data = []

# strip \n and append to data
# data = [x.strip() for x in dI.readlines()] # another way to do add input data to array
for i in dI:
    value = i.strip()
    data.append(value)

dI.close()

# function for counting number of trees encountered during the traversing of the map
# Part 1 and part 2 are solved in the same function using the conditions arr, xInc and yInc


def countTrees(arr, xInc, yInc):
    treeCount = 0
    x = 0
    rowWidth = len(arr[0])
    arrLen = len(arr)

    for row in range(arrLen):
        # print(y)
        print(row % yInc)
        if (row % yInc != 0):
            continue
        if (arr[row][x] == '#'):
            treeCount += 1

        x = (x + xInc) % rowWidth

    return treeCount


# call countTrees function for part 1 and part 2
print('Part 1:', countTrees(data, 3, 1))
print('Part 2:', countTrees(data, 1, 1)*countTrees(data, 3, 1) *
      countTrees(data, 5, 1)*countTrees(data, 7, 1)*countTrees(data, 1, 2))


# Initial code for Part 1
# trees = 0
# x = 0
# forestWidth = len(data[0])

# for j in range(len(data)):

#    if (data[j][x] == '#'):
#        trees += 1
#        print(j, data[j][x])

#    print(x)
#    x = (x + 3) % forestWidth
#    print(x)

# print(trees)
