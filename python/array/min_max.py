# n개의 정수. 최대값 최소값 출력

import sys

a = map(int,sys.stdin.readline().rstrip())

arr =list(map(int, sys.stdin.readline().split()))

min = arr[0]
max = arr[0]

for i in arr:
    if min > i:
        min = i
    if max <i:
        max = i

print(min)
print(max)