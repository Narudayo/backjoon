# 10개 변수 받음. 그것들 42로 나누고 서로 다른 나머지값 몇개 있는지 출력

import sys

d= {}   # 입력값 저장 배열

for i in range(10):
    r = int(sys.stdin.readline().rstrip())%42  
    if r in d:      #   딕셔너리 문법. d에 r이 있다면 true
        d[r] = d[r]+1   
    else:           # 없으면 새로운 dictionary 생성
        d[r]=0

print(len(d))       # dic의 길이 출력. 정답.

