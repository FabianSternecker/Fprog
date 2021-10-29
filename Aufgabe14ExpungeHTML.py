import sys

source = open(sys.argv[1])
target = open(sys.argv[2],"w")
isCode = False

for line in source:
    for c in line:
        if c == "<" or c == ">":
            isCode = not isCode
            continue
        if not isCode:
            target.write(c);

target.close()
source.close()
