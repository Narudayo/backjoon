#백준 2675번 문자열 반복
import sys
input = sys.stdin.readline

#str을 num만큼 반복한 문자열을 return
def printIter(str,num):
    dump = ''
    for s in str:
        dump += s*num
    return dump

T = int(input())

for i in range(T):
    val = input().rstrip().split(' ')
    R = int(val[0])
    S = val[1]
    print(printIter(S,R))


