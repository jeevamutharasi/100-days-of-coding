if __name__ == '__main__':
    N = int(input())
    a = []

for i in range(N):
    c = input().split()
    #print command
    if c[0] == 'insert':
        a.insert(int(c[1]), int(c[2]))
    elif c[0] == 'append':
        a.append(int(c[1]))
    elif c[0] == 'remove':
        a.remove(int(c[1]))
    elif c[0] == 'pop':
        a.pop()
    elif c[0] == 'sort':
        a.sort()
    elif c[0] == 'reverse':
        a.reverse()
    elif c[0] == 'index':
        print(a.index(c[1]))
    elif c[0] == 'count':
        print(a.count(c[1]))
    else:
        print(a)