# https://adventofcode.com/2022/day/3

import string
# part 1
values = dict()
for index, letter in enumerate(string.ascii_letters):
   values[letter] = index + 1

file1 = open('day3/input.txt', 'r')
Lines = file1.readlines()
priority = [0,0]
m = 0
for line in Lines:
   temp = line.replace("\n","")
   num = int(len(temp)/2)
   first = list(temp[:num])
   second = list(temp[(num * -1):])
   class Breakit(Exception): pass
   try:
      for i in first:
         for k in second:
            if i == k:
               priority[0] += values[k]
               raise Breakit
   except Breakit:
      pass
   #part 2
   m += 1
   if m == 1:
      one = list(line)
   elif m == 2:
      two = list(line)
   elif m == 3:
      three = list(line)
      lettone = []
      letttwo = []
      try:
         for j in one:
            for k in two:
               if j == k:
                  lettone.append(k)
            for m in three:
               if j == m:
                  letttwo.append(m)
         for z in lettone:
            for s in letttwo:
               if z == s:
                  priority[1] += values[s]
                  raise Breakit
      except Breakit:
         pass
      m = 0
print(f"Part 1:{priority[0]}\nPart 2:{priority[1]}")