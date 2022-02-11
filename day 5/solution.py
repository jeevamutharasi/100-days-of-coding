n =int(input())
l = []
for i in range(n):
    k = input()
    l.append(k)
s = []
for i in l:
    if i not in s:
        s.append(i)

r =[]
for a in s:
    b = l.count(a)
    r.append(str(b))

print(len(s))
print(' '.join(r))