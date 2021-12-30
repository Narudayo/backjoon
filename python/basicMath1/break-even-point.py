# 백준 1712 손익분기점

import sys
input = sys.stdin.readline
# a : 고정비용, b : 가변비용 , c : 상품 가격

a,b,c = map(int, input().split())

net_income = c-b #순수익
earn_income = 0 #번 돈

if net_income <= 0 : # 순수익이 0 or 음수면 
    print(-1)
else:
    # N = 상품 판매 갯수
    N = a / net_income  
    N += 1
    print(int(N))
    
    