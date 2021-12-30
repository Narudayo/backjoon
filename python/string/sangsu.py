#백준 2908번 상수

import sys
input = sys.stdin.readline

a = list(map(str,input().split()))

rev_a = int(a[0][::-1])
rev_b = int(a[1][::-1])

if rev_a > rev_b:
    print(rev_a)
else:
    print(rev_b)