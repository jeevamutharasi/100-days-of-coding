import itertools
N=int(input("Enter the no. of queens:"))
sol=0
cols=range(N)

for entry in itertools.permutations(cols):

  if N==(len(set(entry[j]+j for j in cols)))==(len(set(entry[j]-j for j in cols))):

    sol+=1
    print(f"Solution {sol} : {entry}")
    print('\n'.join('x'*i+'Q'+'x'*(N-i-1)for i in entry)+"\n\n\n")