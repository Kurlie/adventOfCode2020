# Read Input data file and store in an array
dI = open("day9Input.txt", "r")

# array to store input data
data = []

# strip \n and append to data
for i in dI:
    # dealing with integers so lets make the values in data integers
    data.append(int(i.replace("\n", "")))

dI.close()
# print(data)


def weaknessXMAS(list, peambleLen):
    def check(num):
        for j in preamble:
            if ((num-j) in preamble and ((num-j) != j)):
                return False
        return True

    numbers = list[peambleLen:]
    for i in range(len(numbers)):
        # i is the start of the list 1 after end of preamble
        preamble = list[i:i+peambleLen]

        if (check(numbers[i])):
            return numbers[i]


#print(weaknessXMAS(data, 25))


def encWeakness(list, indexCheck):
    for i in range(len(list[:list.index(indexCheck)])):
        sumContiguousSet = 0
        contiguousSetLen = 2

        while sumContiguousSet < indexCheck:
            contiguousSet = list[i:i+contiguousSetLen]
            sumContiguousSet = sum(contiguousSet)
            contiguousSetLen += 1

        if (sumContiguousSet == indexCheck):
            return min(contiguousSet) + max(contiguousSet)


print("part 1:", weaknessXMAS(data, 25))
print("part 2:", encWeakness(data, weaknessXMAS(data, 25)))
