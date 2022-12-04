file1 = open("input.txt","r")
Lines = file1.readlines()
count = 0
# part 1
for line in Lines:
    a = line.replace("\n", "").split(",")
    groups = []
    for i in a:
        minMax = i.split("-")
        groups.append(minMax)
    if int(groups[1][0]) <= int(groups[0][0]) and int(groups[0][1]) <= int(groups[1][1]):
        count += 1
    elif int(groups[0][0]) <= int(groups[1][0]) and int(groups[1][1]) <= int(groups[0][1]):
        count += 1
print(count)
# part 2
count = 0
for line in Lines:
    a = line.replace("\n", "").split(",")
    groups = []
    first = []
    second = []
    for i in a:
        minMax = i.split("-")
        groups.append(minMax)
    if int(groups[0][0]) == int(groups[0][1]):
        first = [int(groups[0][0])]
    elif int(groups[0][0]) != int(groups[0][1]):
        first.append(int(groups[0][0]))
        for n in range(int(groups[0][1])):
            first.append(first[-1]+1)
            if first[-1] == int(groups[0][1]):
                break
    if int(groups[1][0]) == int(groups[1][1]):
        second = [int(groups[1][0])]
    elif int(groups[1][0]) != int(groups[1][1]):
        second.append(int(groups[1][0]))
        for n in range(int(groups[1][1])):
            second.append(second[-1]+1)
            if second[-1] == int(groups[1][1]):
                break
    for k in first:
        if k in second:
            count += 1
            break
print(count)
