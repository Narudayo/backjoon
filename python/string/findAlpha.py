# 백준 10809번 알파벳 찾기

# 참고 키워드: enumerate

import sys, string

# 배열 arr에 param이 존재하는지
def is_exist(arr,param):
    for i in arr:
        if(i==param):
            return True
    return False

input = sys.stdin.readline
str = input()
alpha = list(string.ascii_lowercase)
find = False

exist = []

for a in alpha:
    # print("{}일때".format(a), end=": ")
    for ind,m in enumerate(str):
        if a==m:
            find=True
            if not is_exist(exist,a):   #만약 이미 처리했던 알파벳이면
                exist.append(a)
                print(ind, end=' ')        
    if find:
        find = False
        continue
    print(-1, end= ' ')