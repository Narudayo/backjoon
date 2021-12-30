import sys

def score(str):
    count = 0
    sum = 0
    for i in range(len(str)):
        if str[i]=="O":
            count +=1
        else :
            count = 0
        sum += count
    return sum

a = int(sys.stdin.readline().rstrip())

for i in range(a):
    str = sys.stdin.readline().rstrip()
    print(score(str))






