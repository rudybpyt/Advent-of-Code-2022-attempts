# https://adventofcode.com/2022/day/1

# part 1
file1 = open('input.txt', 'r')
Lines = file1.readlines()
totalCalories = []
temp = 0
for line in Lines:
    if line == "\n":
        totalCalories.append(temp)
        temp = 0
    else:
        temp += int(line)
totalCalories.sort()
print(f"highest calories is :{totalCalories[-1]}")
# part 2
top3 = totalCalories[-1] + totalCalories[-2] + totalCalories[-3]
print(f"top 3 total : {top3}")
