# 백준 1316번 그룹 단위 체커

# [1] 이전에 봤던 알파벳 prev 현재 보는 알파벳 curr,
# [2] prev = curr 일때는 문제없이 진행.
# [3] prev != curr 일때는 a를 checklist에 append.
# [4] 반복문 처음에 checklist에 curr가 있는지 체크. 만약 있다면 그룹 단어가 아님.
# 오류가 없었다면 그룹단어.

import sys

# string을 받아서 그것이 그룹단어? True : False 반환
def is_checker(string):
    checklist = ''
    prev = ''
    for idx,s in enumerate(string):
        curr = s
        # print('문자 {0}일때 checklist : {1}'.format(s,checklist) )
        if idx == 0: # 처음 index일 때
            if len(string) == 1:    # 한 단어짜리 string일 땐 그룹단어.
                return True
            else:
                checklist += curr
                pass
        else:
            if prev == curr:    # 단어가 그대로일 때
                pass
            else:               # 단어가 바뀌었을 때
                if checklist.find(curr) != -1:  # 이전에 나왔던 단어라면
                    return False
                else:                           # 이전에 나오지 않은 단어라면
                    checklist += curr       # checklist에 추가.
        prev = s
    return True # 아무일도 없었다면 그룹단어가 맞음.


input = sys.stdin.readline

N = int(input().rstrip())
count = 0
for _ in range(N):
    string = input().rstrip()
    # print(is_checker(string))
    if is_checker(string):
        count += 1
print(count)