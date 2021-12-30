import sys
input = sys.stdin.readline

length = int(input())
num = input()
sum = 0

for i in range(length):    
    sum += int(num[i])

print(sum)