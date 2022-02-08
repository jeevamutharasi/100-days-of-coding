def minion_game(string):
    # your code goes here
    p1 =0
    p2=0
    vowel = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(string)):
        if string[i] in vowel:
            p1+= len(string)-i
        else:
            p2+=len(string)-i
    
    if p1>p2:
        print ("Kevin",p1)
    elif p2>p1:
        print ("Stuart",p2)
    else:
        print ("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)