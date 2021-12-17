# 9개의 자연수 중, 최댓값을 찾고 그것이 몇번째 수인지 출력

import sys

arr=[]
# arr =list(map(int, sys.stdin.readline().split()))

for i in range(9):
    arr.append(int(sys.stdin.readline().strip()))
    # print(arr)
    if i==0:
        max = arr[0]
        count = 0
    if max < arr[i]:
        max = arr[i]
        count = i

print(max)
print(count+1)
