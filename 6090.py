a, m, d, n = map(int, input().split( ))
for i in range(n):
    if(i==0):
        result = a
    else:
        result = result*m+d
print(result)
