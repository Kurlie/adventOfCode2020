# Bring in test data
dI = open("day1Input.txt", "r")

data = []

for i in dI:
    value = int(i.strip())
    data.append(value)

dI.close()

# sort array from smallest to largest
data.sort()

# define variables used in while loop
start = 0
end = len(data) - 1
s = 2020
r = 0

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
print(data[start], data[end], data[start] + data[end])
print(r)

check = 0
item = 0
r2 = 0
start2 = 0
end2 = len(data) - 1

for i in data:
    for j in reversed(data):
        #print(i, j)
        check = s - i - j
        if (check in data):
            print('first for loop value', i, ',2nd for loop value', j,
                  ', answer, fist, 2nd and difference between sum', i * j * check)
