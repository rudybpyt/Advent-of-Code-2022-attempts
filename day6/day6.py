# https://adventofcode.com/2022/day/6

file1 = open("day6/input.txt","r")
Line = list(file1.readline())
# part 1
thing = []
count = 0
c = 0
for i in range(len(Line)):
    temp = [Line[i],Line[i+1],Line[i+2],Line[i+3]]
    count = 0
    for k in temp:
        for l in range(len(temp)):
            if k == temp[l]:
                count += 1
    thing.append(count)
    if thing[-1] == 4:
        print(temp)
        print(f"Part 1:{i+4}")
        break
# part 2
thing = []
for i in range(len(Line)):
    temp = []
    for a in range(14):
        temp.append(Line[i+a])
    count = 0
    for k in temp:
        for l in range(len(temp)):
            if k == temp[l]:
                count += 1
    thing.append(count)
    if thing[-1] == 14:
        print(temp)
        print(f"Part 2:{i+14}")
        break