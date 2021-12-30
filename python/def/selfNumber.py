# 백준 4673번 문제. 셀프 넘버
# 1. 배열에 constructor가 있는 것들을 저장
# 2. 1~10000까지, 1번 배열에 해당되지 않는 것들을 출력

def constructor(num):
    stringNum = str(num)
    sum = 0
    for i in range(len(stringNum)):
        # print(stringNum[i])
        sum += int(stringNum[i])
    sum += num
    return sum

# arr에 num이 있는지 여부를 반환
def is_exist(num,arr):
    if num in arr:
        return True
    else:
        return False
    
def createArr():
    arr = []    # arr는 생성자가 모여있는 arr
    
    for i in range(10000):
        con = constructor(i)
        if is_exist(con,arr) == False:
            arr.append(con)
    return arr

cunArr = createArr()

for i in range(10000):
    if is_exist(i,cunArr) == False:
        print(i)

