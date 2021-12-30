# a,b,c 곱하고, 계산한 결과에서 각자의 숫자가 몇개씩 들었는지 출력

import sys

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())

result = a*b*c
arr = [0]*10

# print(arr)
str_result = str(result)
# print(type(str_result))
# print(type(result))

for i in str_result:
    arr[int(i)] +=1

for i in arr:
    print(i)
