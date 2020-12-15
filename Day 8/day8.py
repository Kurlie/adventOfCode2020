# Read Input data file and store in an array
dI = open("day8Input.txt", "r")

# array to store input data
data = []

# strip \n and append to data
for i in dI:
    data.append(i.replace("\n", ""))

dI.close()

# print(data)


def stepDetails(step):
    v = step.split()
    return v


accumulator = 0
jump = 0
check = []
for i in range(len(data)):
    if(jump > 0 or jump < 0):
        print(jump)
        if((jump) in check):
            break
        else:
            check.append(jump)
            step = stepDetails(data[jump])
            if(step[0] == 'acc'):
                accumulator = accumulator + int(step[1])
                jump = jump + 1
                continue
            elif(step[0] == 'jmp'):
                jump = jump + int(step[1])
                continue
            elif(step[0] == 'nop'):
                jump = jump + 1
                continue
    elif(jump == 0):
        print(i)
        if(i in check):
            break
        else:
            check.append(i)
            step = stepDetails(data[i])
            if(step[0] == 'acc'):
                accumulator = accumulator + int(step[1])
                jump = 1
                continue
            elif(step[0] == 'jmp'):
                jump = int(step[1])
                continue
            elif(step[0] == 'nop'):
                jump = 1
                continue

print(accumulator)
