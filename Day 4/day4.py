import re
# Read Input data file and store in an array
dI = open("day4Input.txt", "r")

# print(dI.read())

# array to store input data
data = dI.read().split("\n\n")
# data.append(dI.read().split("\n\n"))

dI.close()

# for i in data[0]:
#    print(i)


def byValidation(by):
    # birth year validation
    invalid = 0
    byStartIndex = by.find("byr:")

    if (byStartIndex == -1):
        invalid = 1
    else:
        byEndIndex = by.find(" ", byStartIndex, len(by))
        if (byEndIndex == -1):
            test = by[byStartIndex+4: len(by)]
        else:
            test = by[byStartIndex+4:byEndIndex]
        if (len(test) != 4):
            invalid = 1
        elif (int(test) < 1920 or int(test) > 2002):
            invalid = 1

    return invalid


def iyValidation(by):
    # issue year validation
    invalid = 0
    byStartIndex = by.find("iyr:")

    if (byStartIndex == -1):
        invalid = 1
    else:
        byEndIndex = by.find(" ", byStartIndex, len(by))
        if (byEndIndex == -1):
            test = by[byStartIndex+4: len(by)]
        else:
            test = by[byStartIndex+4:byEndIndex]
        if (len(test) != 4):
            invalid = 1
        elif (int(test) < 2010 or int(test) > 2020):
            invalid = 1

    return invalid


def eyValidation(by):
    # expiration year validation
    invalid = 0
    byStartIndex = by.find("eyr:")

    if (byStartIndex == -1):
        invalid = 1
    else:
        byEndIndex = by.find(" ", byStartIndex, len(by))
        if (byEndIndex == -1):
            test = by[byStartIndex+4: len(by)]
        else:
            test = by[byStartIndex+4:byEndIndex]
        if (len(test) != 4):
            print(test)
            invalid = 1
        elif (int(test) < 2020 or int(test) > 2030):
            invalid = 1

    return invalid


def hValidation(by):
    # height validation function
    import re
    invalid = 0
    m = re.search('hgt:[\d]+cm|in ', by)

    if (m is None):
        invalid = 1
    else:
        byStartIndex = by.find("hgt:")
        byEndIndex = by.find(" ", byStartIndex, len(by))
        if (byEndIndex == -1):
            test = by[byStartIndex+4: len(by)]
        else:
            test = by[byStartIndex+4:byEndIndex]
        indexCM = test.find("cm")
        indexIN = test.find("in")
        if(indexCM > 0):
            # might need to be -1 for end of substring in following if statement
            if (int(test[:indexCM]) < 150 or int(test[:indexCM]) > 193):
                invalid = 1
        elif(indexIN > 0):
            # might need to be -1 for end of substring in following if statement
            if (int(test[:indexIN]) < 59 or int(test[:indexIN]) > 76):
                invalid = 1

    return invalid


def hcValidation(by):
    import re
    invalid = 0
    byStartIndex = by.find("hcl:")

    if (byStartIndex == -1):
        invalid = 1
    else:
        m = re.search('hcl:#[\da-f]{6} ', by)
        if(m is None):
            invalid = 1
    return invalid


def ecValidation(by):
    invalid = 0
    byStartIndex = by.find("ecl:")

    if (byStartIndex == -1):
        invalid = 1
    else:
        byEndIndex = by.find(" ", byStartIndex, len(by))
        if (byEndIndex == -1):
            test = by[byStartIndex+4: len(by)]
        else:
            test = by[byStartIndex+4:byEndIndex]
        check = "amb blu brn gry grn hzl oth"
        if (test not in check):
            invalid = 1

    return invalid


def pidValidation(by):
    invalid = 0
    byStartIndex = by.find("pid:")

    if (byStartIndex == -1):
        invalid = 1
    else:
        byEndIndex = by.find(" ", byStartIndex, len(by))
        if (byEndIndex == -1):
            test = by[byStartIndex+4: len(by)]
        else:
            test = by[byStartIndex+4:byEndIndex]
        if (len(test) > 9):
            invalid = 1
        elif(test.isdigit() == False):
            invalid = 1

    return invalid


def passportCheck(arr):

    check = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    valid = 0
    count = 0
    passportRFPass = []

    for i in arr:
        count = 0
        p = i.replace("\n", " ")
        for j in check:
            if (j in i):
                # print(j, i)
                count += 1

        if (count == 7):
            valid += 1
            passportRFPass.append(p)

    return valid, passportRFPass


def part2(arr):
    valid = 0
    #numPassports = 0
    for i in arr:
        p = i.replace("\n", " ")
        if (byValidation(p) + iyValidation(p) + eyValidation(p) + hValidation(p) + hcValidation(p) + ecValidation(p) + pidValidation(p) == 0):
            valid += 1

    return valid


# I want to fix this
# print(part2(passportCheck(data)[1]))

### -------------------------------------------- ###
### -------------------------------------------- ###

# Part 1
print(passportCheck(data)[0])

### -------------------------------------------- ###
### -------------------------------------------- ###
# part 2
vp = 0

for i in data:
    p = i.replace("\n", " ")
    v = 0
    for j in p.split():
        if (j[0:3] == "byr"):
            # print(j)
            byr = j[4:len(j)]
            if (len(byr) == 4 and 1920 <= int(byr) <= 2002):
                v += 1
                #print(j[4:len(j)], v)
        elif (j[0:3] == "iyr"):
            iyr = j[4:len(j)]
            if (len(iyr) == 4 and 2010 <= int(iyr) <= 2020):
                v += 1
        elif (j[0:3] == "eyr"):
            eyr = j[4:len(j)]
            if (len(eyr) == 4 and 2020 <= int(eyr) <= 2030):
                v += 1
        elif (j[0:3] == "hgt"):
            if (j[-2:] == "in"):
                if(59 <= int(re.sub('[^0-9]', '', j)) <= 76):
                    v += 1
            elif (j[-2:] == "cm"):
                if(150 <= int(re.sub('[^0-9]', '', j)) <= 193):
                    v += 1
        elif (j[0:3] == "hcl"):
            if(re.match(r"hcl:#[a-f0-9]{6}$", j)):
                v += 1
        elif (j[0:3] == "ecl"):
            ecl = j[4:len(j)]
            if (ecl in "amb blue brn gry grn hzl oth"):
                v += 1
        elif (j[0:3] == "pid"):
            if(re.match(r"pid:[0-9]{9}$", j)):
                v += 1
    if (v == 7):
        vp += 1
    #print(p, v, vp)

#        print(v)

print(vp)
