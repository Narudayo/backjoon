#백준 2941번 크로아티아

import sys
input = sys.stdin.readline

croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']

# 문자열에서 croa에 해당되는 부분이 있으면 빼서 분해,
# 나머지 일반 문자들 append.

str = input().rstrip()
splitList = []

for c in croa:
    for _ in range(str.count(c)):
        splitList.append(c)
        str = str.replace(c,' ',1)  
        # 그냥 붙이면 새로운 크로아티아 문자가 생성되는 현상이 있어서 공백으로 list 구분.
    
for s in str:
    if s != ' ':
        splitList.append(s)

# print(splitList)
print(len(splitList))

