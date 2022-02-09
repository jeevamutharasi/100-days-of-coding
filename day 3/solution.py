def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        s=string[i:i+k]
        a=""
        for i in s:
            if i not in a:           
                a=a+i
        print(a)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)