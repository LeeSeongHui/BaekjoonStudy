D = [[0 for _ in range(101)] for _ in range(101)]

cnt = 0
N = int(input())
for _ in range(N):
    x,y = map(int,input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            D[i][j] = 1

for s in D:
    cnt+=s.count(1)
print(cnt)