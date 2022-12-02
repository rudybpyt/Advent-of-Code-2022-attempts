# https://adventofcode.com/2022/day/2
# A rock, B paper, C scissors
# X rock, Y paper, Z scissors
# 1 rock, 2 paper, 3 scissors
# 0 lost, 3 draw, 6 win
# part 1
file1 = open('input.txt', 'r')
Lines = file1.readlines()
totalScore = 0
for line in Lines:
    if line.startswith("A") and line.endswith("Y\n"):
        totalScore += 8
    elif line.startswith("B") and line.endswith("Z\n"):
        totalScore += 9
    elif line.startswith("C") and line.endswith("X\n"):
        totalScore += 7
    elif line.startswith("A") and line.endswith("X\n"):
        totalScore += 4
    elif line.startswith("B") and line.endswith("Y\n"):
        totalScore += 5
    elif line.startswith("C") and line.endswith("Z\n"):
        totalScore += 6
    elif line.endswith("X\n"):
        totalScore += 1
    elif line.endswith("Y\n"):
        totalScore += 2
    elif line.endswith("Z\n"):
        totalScore += 3
print(totalScore)
# X lose, Y draw, Z win
totalScore2 = 0
for line in Lines:
    if line.endswith("X\n"):
        if line.startswith("A"):
            totalScore2 += 3
        if line.startswith("B"):
            totalScore2 += 1
        if line.startswith("C"):
            totalScore2 += 2
    elif line.endswith("Y\n"):
        if line.startswith("A"):
            totalScore2 += 4
        if line.startswith("B"):
            totalScore2 += 5
        if line.startswith("C"):
            totalScore2 += 6
    elif line.endswith("Z\n"):
        if line.startswith("A"):
            totalScore2 += 8
        if line.startswith("B"):
            totalScore2 += 9
        if line.startswith("C"):
            totalScore2 += 7
print(totalScore2)
