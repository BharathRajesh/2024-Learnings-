name1="rajesh"
name2="lakshmi"
nam=(name1+name2).lower()
t,r,u,e=nam.count("t"),nam.count("r"),nam.count("u"),nam.count("e")
l,o,v,e=nam.count("l"),nam.count("o"),nam.count("v"),nam.count("e")
p1=t+r+u+e
p2=l+o+v+e
p=str(p1)+str(p2)
print(f"{p}%")