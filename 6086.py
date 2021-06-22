num = int(input())
sum = 0
for i in range(1, num+1):
    if(sum < num):
        sum += i
    else:
        break
print(sum)
