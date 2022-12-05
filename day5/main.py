import array
# part 1
file1 = open("input.txt","r")
Lines = file1.readlines()
i = 0
cols =[[],[],[],[],[],[],[],[],[]]

for line in Lines:
    i += 1
    print(i)
    if i <= 8:
        temp = list(line)
        if len(temp) > 0:
            if temp[1] != " ":
                cols[0].append(temp[1])
            if temp[5] != " ":
                cols[1].append(temp[5])
            if temp[9] != " ":
                cols[2].append(temp[9])
            if temp[13] != " ":
                cols[3].append(temp[13])
            if temp[17] != " ":
                cols[4].append(temp[17])
            if len(temp) >= 32:
                if temp[21] != " ":
                    cols[5].append(temp[21])
                if temp[25] != " ":
                    cols[6].append(temp[25])
                if temp[29] != " ":
                    cols[7].append(temp[29])
                if len(temp) >= 35:
                    if temp[33] != " ":
                        cols[8].append(temp[33])
            print(cols)
    if i == 9:
        for x in range(9):
            cols[x].reverse()
            print(f"hello  {cols}")
    if i > 10:
        temp = line.split()
        size = int(temp[1])
        fromcol = int(temp[3])-1
        tocol = int(temp[5])-1
        print(size,fromcol,tocol)
        for x in range(size):
            cols[tocol].append(cols[fromcol][-1])
            cols[fromcol].pop(-1)
        print(cols)
# part 2
i = 0
cols =[[],[],[],[],[],[],[],[],[]]
for line in Lines:
    i += 1
    print(i)
    if i <= 8:
        temp = list(line)
        if len(temp) > 0:
            if temp[1] != " ":
                cols[0].append(temp[1])
            if temp[5] != " ":
                cols[1].append(temp[5])
            if temp[9] != " ":
                cols[2].append(temp[9])
            if temp[13] != " ":
                cols[3].append(temp[13])
            if temp[17] != " ":
                cols[4].append(temp[17])
            if len(temp) >= 32:
                if temp[21] != " ":
                    cols[5].append(temp[21])
                if temp[25] != " ":
                    cols[6].append(temp[25])
                if temp[29] != " ":
                    cols[7].append(temp[29])
                if len(temp) >= 35:
                    if temp[33] != " ":
                        cols[8].append(temp[33])
            print(cols)
    if i == 9:
        for x in range(9):
            cols[x].reverse()
            print(f"hello  {cols}")
    if i > 10:
        temp = line.split()
        size = int(temp[1])
        fromcol = int(temp[3])-1
        tocol = int(temp[5])-1
        print(size,fromcol,tocol)
        for x in range(size):
            cols[tocol].append(cols[fromcol][(-1 * size)+ x])
            cols[fromcol].pop((-1 * size)+ x)
        print(cols)
