# part 1
file1 = open("input.txt","r")
Lines = file1.readlines()
i = 0
cols =[[],[],[],[],[],[],[],[],[]]
cols2 =[[],[],[],[],[],[],[],[],[]]
output = ""
output2 = ""
for line in Lines:
    i += 1
    if i <= 8:
        temp = list(line)
        if len(temp) > 0:
            if temp[1] != " ":
                cols[0].append(temp[1])
                cols2[0].append(temp[1])
            if temp[5] != " ":
                cols[1].append(temp[5])
                cols2[1].append(temp[5])
            if temp[9] != " ":
                cols[2].append(temp[9])
                cols2[2].append(temp[9])
            if temp[13] != " ":
                cols[3].append(temp[13])
                cols2[3].append(temp[13])
            if temp[17] != " ":
                cols[4].append(temp[17])
                cols2[4].append(temp[17])
            if len(temp) >= 32:
                if temp[21] != " ":
                    cols[5].append(temp[21])
                    cols2[5].append(temp[21])
                if temp[25] != " ":
                    cols[6].append(temp[25])
                    cols2[6].append(temp[25])
                if temp[29] != " ":
                    cols[7].append(temp[29])
                    cols2[7].append(temp[29])
                if len(temp) >= 35:
                    if temp[33] != " ":
                        cols[8].append(temp[33])
                        cols2[8].append(temp[33])
    if i == 9:
        for x in range(9):
            cols[x].reverse()
            cols2[x].reverse()
    if i > 10:
        temp = line.split()
        size = int(temp[1])
        fromcol = int(temp[3])-1
        tocol = int(temp[5])-1
        for x in range(size):
            cols[tocol].append(cols[fromcol][-1])
            cols[fromcol].pop(-1)
            # part 2 
            cols2[tocol].append(cols2[fromcol][(-1 * size)+ x])
            cols2[fromcol].pop((-1 * size)+ x)
for i in range(len(cols)):
    output += cols[i][-1]
    output2 += cols2[i][-1]
print(f"Part 1:{output}")
print(f"Part 2:{output2}")
