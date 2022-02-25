n,m=input().split()
sett=input().split()
A=set(input().split())
B=set(input().split())
h=0

for i in sett:
    if i in A:
        h+=1
    elif i in B:
        h-=1
    else:
        pass
print(h) 