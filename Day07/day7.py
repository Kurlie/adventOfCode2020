# Read Input data file and store in an array
dI = open("day7Input.txt", "r")

# dictionary to store input data
data = {}

# data manipulation to get input to dictionary
for i in dI:
    value = i.strip()
    value = value.replace("bags", "bag").replace("bag", "").replace(".", "")
    value = " ".join(value.split()).replace(" ,", ",")
    contains = value[value.find("contain ")+8:]
    each_cnt = contains.replace(", ", ",").split(",")
    each_cnt = {" ".join(cont.split(" ")[1:]): cont.split(" ")[
        0] for cont in each_cnt}
    # print(each_cnt)
    # data.update(" ".join(value.split(" ")[:2]): each_cnt)
    data[" ".join(value.split(" ")[:2])] = each_cnt
    # data.append(value)

dI.close()

# print(data["shiny gold"].items())


def countBags(allBags, bagCheck, currentBag):
    #print(allBags[currentBag].items(), currentBag, bagCheck)
    if(currentBag == bagCheck):
        return 1
    if(allBags.get(currentBag) is None):
        return 0
    else:
        total = []
        for k, v in allBags[currentBag].items():
            total.append(countBags(allBags, bagCheck, k))
        # print(total, max(total))
        return max(total)


totalBags = 0
bagCheck = "shiny gold"
for k, v in data.items():
    print(k, v.values())
    if k != bagCheck:
        totalBags += countBags(data, bagCheck, k)
print(f"{totalBags} bags can contain {bagCheck} bag.")
