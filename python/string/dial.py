#백준 5622번 다이얼

import sys, string
input = sys.stdin.readline

# (알파벳 : 숫자)를 입력할 더 좋은 식이 생각 안나는 중.
alpha = list(string.ascii_uppercase)
count = 2

al_num = {}

for a in alpha:
    al_num[a] = count
    if a == 'C':
        count += 1
    if a == 'F':
        count += 1
    if a == 'I':
        count += 1
    if a == 'L':
        count += 1
    if a == 'O':
        count += 1
    if a == 'S':
        count += 1
    if a == 'V':
        count += 1
    if a == 'Z':
        count += 1

num_time = {}
count = 2

for i in range(1,10):
    num_time[i] = count
    count +=1

str = input().rstrip()
sum = 0
for s in str:
    sum += num_time[al_num[s]]

print(sum)