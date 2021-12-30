# 백준 1065번 문제. 한수

# 차수를 n이라고 하자. n이 일정하면 등차수열. 등차수열이면 한수
# 한수의 개수 출력.

import sys


# num을 받아 degree를 알려주는 함수.
def find_degree(num):
    if num >= 10:    # 10보다 큰 경우만 등차수열 판단 가능.
        strN = str(num)
        a = int(strN[0])
        b = int(strN[1])
        return b-a
    else:
        return num
    

# num이 한수인지 아닌지를 판단
def is_hansu(num):
        degree = find_degree(num)
        strN = str(num)
        for i in range(len(strN)-1):
            if (int(strN[i+1])-int(strN[i])) != degree:
                return False
        return True

count = 0
a = int(sys.stdin.readline().rstrip())

for i in range(1,a+1):
    if is_hansu(i):
        count+=1

print(count)