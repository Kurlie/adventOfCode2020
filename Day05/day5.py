import math
# Read Input data file and store in an array
dI = open("day5Input.txt", "r")

# print(dI.read())

# array to store input data
data = dI.read().split("\n")
# data.append(dI.read().split("\n\n"))

dI.close()

# print(data)


def findRow(str, lb, ub):
    # str should be length of 7
    # lb start at 0
    # up start at 127
    row = 0
    lbRow = lb
    ubRow = ub
    check = ""

    for i in str[:len(str)]:
        if(i == "F"):
            ubRow = ubRow - ((ubRow - lbRow) / 2)
            ubRow = math.floor(ubRow)
            check = "L"
            # print(ubRow)
        elif(i == "B"):
            lbRow = lbRow + ((ubRow - lbRow) / 2)
            lbRow = math.ceil(lbRow)
            check = "U"
            # print(lbRow)
        #print(lbRow, ubRow)

    if (check is "L"):
        row = lbRow
    elif (check is "U"):
        row = ubRow

    return row


print(findRow("FBFBBFF", 0, 127))


def findColumn(str, lb, ub):
    # str should be length of 3
    column = 0
    lbColumn = lb  # start at 0
    ubColumn = ub  # start at 7
    check = ""

    for i in str[:len(str)]:
        if(i == "L"):
            ubColumn = ubColumn - ((ubColumn - lbColumn) / 2)
            ubColumn = math.floor(ubColumn)
            check = "L"
            # print(ubColumn)
        elif(i == "R"):
            lbColumn = lbColumn + ((ubColumn - lbColumn) / 2)
            lbColumn = math.ceil(lbColumn)
            check = "U"
            # print(lbColumn)
        #print(lbColumn, ubColumn)

    if (check is "L"):
        column = lbColumn
    elif (check is "U"):
        column = ubColumn

    return column


print(findColumn("RLR", 0, 7))


def seatID(row, column):
    return (row * 8) + column


print(seatID(findRow("FBFBBFF", 0, 127), findColumn("RLR", 0, 7)))


def mySeat(arr):
    # list comprehensions found https://docs.python.org/3/tutorial/datastructures.html  section 5.1.3
    # in our case we know it will be 1 value in the list
    return [x for x in range(arr[0], arr[-1]+1)
            if x not in arr]


def highestSeatID(data):
    storeSeatID = 0
    seatList = []
    for i in data:
        row = findRow(i[:7], 0, 127)
        column = findColumn(i[-3:], 0, 7)
        seat = seatID(row, column)
        seatList.append(seat)
        if (seat > storeSeatID):
            storeSeatID = seat
    seatList.sort()
    return storeSeatID, mySeat(seatList)


print(highestSeatID(data))
