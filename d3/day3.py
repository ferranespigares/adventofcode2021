with open("d3/input") as f:
    lines = f.readlines()
res=[0,0,0,0,0,0,0,0,0,0,0,0]
def cgamma(iv):
    if iv<0:
        return "0"
    else:
        return "1"
def cepsilon(iv):
    if iv<0:
        return "1"
    else:
        return "0"
for l in lines:
    for j in range(12):
        if l[j]=="0":
            res[j]=res[j]-1
            continue
        else:
            res[j]=res[j]+1
g=[c for c in map(cgamma,res)]
e=[c for c in map(cepsilon,res)]
gamma=int("".join(g),2)
epsilon=int("".join(e),2)
print("Part1:",gamma*epsilon)
