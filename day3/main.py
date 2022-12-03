import string

values = dict()
for index, letter in enumerate(string.ascii_letters):
   values[letter] = index + 1

file1 = open('input.txt', 'r')
Lines = file1.readlines()
priority = 0
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
               priority += values[k]
               raise Breakit
   except Breakit:
      pass
print(priority)

priority = 0
i = 0
for line in Lines:
   i += 1
   if i == 1:
      one = list(line)
   elif i == 2:
      two = list(line)
   elif i == 3:
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
                  priority += values[s]
                  raise Breakit
      except Breakit:
         pass
      i = 0
print(priority)