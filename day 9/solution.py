T = int(input())
for i in range(T):
    N, X = map(int, input().split())
    friends = [1]*N
    routine = []
    res = 0
    for j in range(N):
        arrival, departure = map(int, input().split())
        routine.append([arrival,departure])
    routine.sort(key= lambda x: x[1])
    for j in range(1, N):
        for k in range(j):
            if routine[j][0] <= routine[k][1]:
                friends[k] +=1
        if len([item for item in friends if item == X]) > 0:
              res +=1
              friends = [item - 1 for item in friends[:j+1]]+friends[j+1:]
    print(res)
