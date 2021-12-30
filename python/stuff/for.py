import sys


n,x = map(int,sys.stdin.readline().split())
for i in map(int,sys.stdin.readline().split()):
    if i < x:
        print(i,end=" ")
# n = int(sys.stdin.readline().rstrip())
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*i)



