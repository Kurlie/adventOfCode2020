# Read Input data file and store in an array
dI = open("day1Input.txt", "r")

# array to store input data
data = []

# strip \n and append to data
for i in dI:
    value = int(i.strip())
    data.append(value)

dI.close()

# sort array from smallest to largest
data.sort()

####--------------------------------------------------------------------------------#####
####--------------------------------------------------------------------------------#####

# part 1 : 2 indexes summed to the value of 2020 multiplied for final
start = 0  # will be used as first index in while loop
end = len(data) - 1  # will be used for last index in while loop
s = 2020  # value to sum indexes to
r = 0  # return variable

# loop through array while start of array is smaller than the end of the array
# testing to determine if 2 values of the array summed equal the value of s
# if they equal, multiple the 2 values to create day 1 answer
# otherwise increment start variable by 1 if the sum is less than the value of s
# else decrease r by a value of 1
while start < end:
    if (data[start] + data[end] == s):
        r = data[start] * data[end]
        break
    elif (data[start] + data[end] < s):
        start += 1
    else:
        end -= 1

# output our answer
# print(data[start], data[end]) # will print indexes used for part 1
print(r)

####--------------------------------------------------------------------------------#####
####--------------------------------------------------------------------------------#####

# part 2 : 3 indexes summed to the value of 2020 multiplied for final
# brute force method

check = 0
r2 = 0  # return variable

for i in data:
    for j in reversed(data):
        # print(i, j)
        check = s - i - j
        if (check in data):  # if value of s (2020) - index 1 - index 2 is an index of data
            # print('index 1:', i, 'and index 2:', j,
            #      'and index 1, 2 and 3 multiplied =', i * j * check)
            r2 = (i * j * check)
            break

print(r2)
