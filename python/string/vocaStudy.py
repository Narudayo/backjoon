import sys
input = sys.stdin.readline

# str ==> 알파벳별로 몇 개씩 들어가 있는지 적힌 dictionary를 반환.
def vocaCount(str):
    str = str.lower()
    dic = {}
    for i in str:
        if dic.get(i) == None:  # dic에 i가 없으면 (처음 값 삽입이면)
            dic[i] = 1
        else:
            dic[i] += 1
    return dic

# dic ==> value값의 최대치를 반환. 같은게 있다면 '?'반환.
def findCount(dic):
    max = 0
    for d in dic.items():
        if max < d[1]:
            max = d[1]
            alpha = d[0]
    valArr = list(dic.values())
    if valArr.count(max) > 1 and len(valArr) > 1:
        return '?'
    else:
        return alpha

string = input().rstrip()
print(findCount(vocaCount(string)).upper())