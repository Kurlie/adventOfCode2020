# Read Input data file and store in an array
dI = open("day6Input.txt", "r")

# print(dI.read())

# array to store input data
data = dI.read().split("\n\n")
# data.append(dI.read().split("\n\n"))

dI.close()


# new array to hold dictionary that replaces \n break
# note, not the best way to do this as I am creating a 2nd array
replaceLineBreak = []
# replace \n in data and append to new array replaceLineBreak
for i in data:
    # print(i)
    p = i.replace("\n", " ")
    replaceLineBreak.append(p)

# part 1
total = 0

for j in replaceLineBreak:
    count = ""
    for k in j:
        if (k not in count):
            count = count + k

    total = total + len(count.replace(" ", ""))

print(total)

# part 2
abc = "abcdefghijklmnopqrstuvwxyz"
total2 = 0
nSpaces = 0

for group in replaceLineBreak:
    count = ""
    # number of people in group is dependent on number of spaces + 1
    nSpaces = group.count(" ")
    # if number of people is 1: all answers (length of group) get added to total answers
    if (nSpaces == 0):
        total2 = total2 + len(group)
    # if more than 1 person: check if letter (in abc) is in all persons answers
    elif (nSpaces > 0):
        # iterate through the alphabet
        for letter in abc:
            # print(letter)
            # find how many persons in group have anserwed yes for letter (in abc)
            nLetter = group.count(letter)
            # check if number of letters in group equal number of people in group
            if (nLetter == nSpaces + 1):
                total2 = total2 + 1

print(total2)
