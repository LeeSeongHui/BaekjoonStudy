chk = 0
location = []
for i in range(9):
    arr = list(map(int,input().split()))
    for j in range(9):
        if arr[j] >= chk:
            chk = arr[j]
            location = [i+1,j+1]
print(chk)
print(' '.join(map(str,location)))