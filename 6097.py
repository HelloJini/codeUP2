h, w = map(int, input().split())
q = []
for i in range(h+1):
    q.append([])
    for j in range(w+1):
        q[i].append(0)

n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if(d==0):
            q[x][y+j] = 1
        else:
            q[x+j][y] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print(q[i][j], end=' ')
    print()