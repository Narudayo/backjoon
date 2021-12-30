import sys

c = int(sys.stdin.readline().rstrip())  # 케이스의 숫자

for i in range(c):
    # n = 0   # 사람의 숫자
    sum = 0 # 점수의 총 값

    arr = list(map(int, sys.stdin.readline().split()))

    for idx, val in enumerate(arr):
        if idx == 0:
            n = val
        else:
            sum += val
    
    aver = sum/n
    count = 0 # 평균을 넘는 과목들의 숫자
    
    for idx, val in enumerate(arr):
        if idx != 0:
            if val > aver:
                count += 1

    result = (count/n*100)

    print('{:.3f}%'.format(result))
    






    # n = 0   # 사람의 숫자
    # sum = 0 # 점수의 총 값

    # arr = list(map(int, sys.stdin.readline().rstrip().split()))
    # if i==0:
    #     n = arr[i]  
    # else :
    #     sum += arr[n]

    # aver = sum/n
    # count = 0 # 평균을 넘는 과목들의 숫자

    # for i in range(len(arr)):
    #     if i != 0:
    #         if aver <arr[i]:
    #             count +=1
    # print("%f"%(count/n))
        
