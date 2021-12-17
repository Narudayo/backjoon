import sys

# while True:
#     try:
#         a,b = map(int, sys.stdin.readline().split())
#         print(a+b)
#     if a==0 and b==0:
#     except:
#             break
    
count = 0
a = sys.stdin.readline().rstrip()
temp = a


if len(a)==1:
    a= '0' + a

while len(a)>1:
    
    # print("temp : {0}".format(temp))
    # print("a : {0}".format(a))
    result = str(int(a[0]) + int(a[1]))
    # print("result length : {0}".format(len(result)))
    # print("result : {0}".format(result))
    if len(result)>1:
        a = a[1] + result[1]
    else :
        a = a[1] + result
    if int(temp)==int(a):break
    count+=1
print(count+1)


# while int(a)>10:
#     # a의 [1] + result. 여기서 result> 10이면 result[1]
#     result = int(a[0]) + int(a[1])
#     print("###%d",result)
#     if result >10:
#         a = int(a[1]) + int(str(result)[1])
#     else :
#         a = int(a[1]) + result
#     count+=1