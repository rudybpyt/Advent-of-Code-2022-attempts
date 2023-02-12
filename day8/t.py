#https://adventofcode.com/2022/day/8

file1 = open("day8/input.txt","r")
Lines = list(file1.readlines())
data =Lines[1:-1]
count = 0

for i in range(len(data)):
    middle = list(map(int, data[i].replace("\n","")))
    middlevalues = middle[1:-1]
    tempr = list(reversed(middle))
    tempb = list(reversed(Lines))
    for l in range(len(middlevalues)):
        print(f"checking {middlevalues[l]}")
        topc = 0 
        leftc = 0 
        rightc = 0
        botc = 0
        top = []
        left= []
        right = []
        bot = []
        if i == 0:
            temp = list(map(int, Lines[0].replace("\n","")))
            top.append(temp[l+1])
        else:
            for k in range(i+1):
                temp = list(map(int, Lines[k].replace("\n","")))
                #print(Lines[k])
                top.append(temp[l+1])         
        
        if i == (len(middlevalues)-1):
            temp = list(map(int, Lines[-1].replace("\n","")))
            bot.append(temp[l+1])
        else:
            for k in range((len(middlevalues)-(i))):
                temp = list(map(int, tempb[k].replace("\n","")))
                #print(Lines[k])
                bot.append(temp[l+1])

        for k in range(len(top)):
            if middlevalues[l] <= top[k]:
                topc += 1
        for k in range(len(bot)):
            if middlevalues[l] <= bot[k]:
                botc += 1
        for k in range(l+1):
            #print(k)
            temp = middle
            left.append(temp[k])
            #print(f"left:{left}")
        for k in range((len(middle)-(l+2))):
            #print(f"comparing:{middlevalues[l]} to:{tempr[k]}")
            right.append(tempr[k])
        for k in range(len(left)):
            #print(f"comparing:{middlevalues[l]} to:{left[k]}")
            if middlevalues[l] <= left[k]:
                leftc += 1
        for k in range(len(right)):
            if middlevalues[l] <= right[k]:
                rightc += 1
        
        if (topc == 0):
            print(f"{middlevalues[l]} is visible from top")
            count += 1
        elif (leftc == 0):
            print(f"{middlevalues[l]} is visible from left")
            count += 1
        elif (rightc == 0):
            print(f"{middlevalues[l]} is visible from right")
            count += 1
        elif (botc == 0):
            print(f"{middlevalues[l]} is visible from bottom")
            count += 1
outside = ((len(Lines)*2)+((len(Lines)*2)-4))
print(f"Part1:{count+outside}")