with open("d2/input") as f:
    lines = f.readlines()
x,y=0,0
for l in lines:
    d,u=l.split(" ")
    if d=="forward":
        x=x+int(u)
        continue
    if d=="down":
        y=y+int(u)
        continue
    if d=="up":
        y=y-int(u)
print("Part1:",x*y)
x,y,a=0,0,0
for l in lines:
    d,u=l.split(" ")
    if d=="forward":
        x=x+int(u)
        y=y+(a*int(u))
        continue
    if d=="down":
        a=a+int(u)
        continue
    if d=="up":
        a=a-int(u)
print("Part2:",x*y)