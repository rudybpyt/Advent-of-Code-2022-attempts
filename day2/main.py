# https://adventofcode.com/2022/day/2
# A rock, B paper, C scissors
# X rock, Y paper, Z scissors
# 1 rock, 2 paper, 3 scissors
# 0 lost, 3 draw, 6 win
# part 1
file1 = open('day2/input.txt', 'r')
Lines = file1.readlines()
totalScore = [0,0]
for line in Lines:
    if line.startswith("A") and line.endswith("Y\n"):
        totalScore[0] += 8
    elif line.startswith("B") and line.endswith("Z\n"):
        totalScore[0] += 9
    elif line.startswith("C") and line.endswith("X\n"):
        totalScore[0] += 7
    elif line.startswith("A") and line.endswith("X\n"):
        totalScore[0] += 4
    elif line.startswith("B") and line.endswith("Y\n"):
        totalScore[0] += 5
    elif line.startswith("C") and line.endswith("Z\n"):
        totalScore[0] += 6
    elif line.endswith("X\n"):
        totalScore[0] += 1
    elif line.endswith("Y\n"):
        totalScore[0] += 2
    elif line.endswith("Z\n"):
        totalScore[0] += 3
    # part 2
    # X lose, Y draw, Z win
    if line.endswith("X\n"):
        if line.startswith("A"):
            totalScore[1] += 3
        if line.startswith("B"):
            totalScore[1] += 1
        if line.startswith("C"):
            totalScore[1] += 2
    elif line.endswith("Y\n"):
        if line.startswith("A"):
            totalScore[1] += 4
        if line.startswith("B"):
            totalScore[1] += 5
        if line.startswith("C"):
            totalScore[1] += 6
    elif line.endswith("Z\n"):
        if line.startswith("A"):
            totalScore[1] += 8
        if line.startswith("B"):
            totalScore[1] += 9
        if line.startswith("C"):
            totalScore[1] += 7
print(f"Part 1:{totalScore[0]}\nPart 2:{totalScore[1]}")