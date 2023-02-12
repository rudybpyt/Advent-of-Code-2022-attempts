# https://adventofcode.com/2022/day/7

file1 = open("day7/i.txt","r")
Lines = list(file1.readlines())
tree=[]
folderhis = []
def index_2d(tree, v):
    for i, x in enumerate(tree):
        if v in x:
            return i, x.index(v)

for line in Lines:
    dat = line.split()
    if(line.startswith("$ cd ")):
        try:
            tree.append(temp)
            print(temp)
            print(tree)
            folderhis.append(indir)
            #indexs = list(index_2d(tree,lastdir))
            #print(indexs)
           # tree[indexs[0]][indexs[1]] = temp
        except:
            temp = []
        temp = []
        indir = dat[-1]
        if indir == "..":
            indir = folderhis[-1]
        temp.append(indir)
    #print(dat)
    if dat[0].isnumeric():
        temp.append(dat[0])
    elif  dat[0] == "dir":
        temp.append(dat[1])
print(tree)
print(folderhis)