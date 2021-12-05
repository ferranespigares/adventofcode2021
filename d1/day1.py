with open("d1/input") as f:
    lines = f.readlines()
ld=99999
i=0
lines=[int(x) for x in lines]
for l in lines:
    if l > ld:
        i=i+1
    ld=l   
print("Part1:",i)

i=0
j=0
ld=999999
while i <= len(lines)-3:
    s=lines[i]+lines[i+1]+lines[i+2]
    if s > ld:
        j=j+1
    ld=s
    i=i+1
print("Part2:",j)