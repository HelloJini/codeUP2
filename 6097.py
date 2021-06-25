d = []
w, h = map(int, input().split( ))
for i in range(h):
    d.append([])
    for j in range(w):
        d[i].append(0)

n = int(input())
for k in range(n):
    l, f, x, y = map(int, input().split())
    x = int(x)
    y = int(y)
    for i in range(h):
        if(f==1):
            d[x+1][y+1] = 1
        for j in range(l):
            if(f==0):
                d[x][y] = 1

for i in range(1, h):
    for j in range(1, w):
        print(d[i][j], end=' ')
    print()