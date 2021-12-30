import sys

a = int(sys.stdin.readline().rstrip())
arr =list(map(int, sys.stdin.readline().split()))

M = arr[0] # 3개중 최대값

for i in arr:
    if M <i:
        M = i

for i in range(0,len(arr)):
    arr[i] = arr[i]/M*100

sum = 0

for i in arr:
    sum += i

# print("M : %d"%M)

print(sum/len(arr))


