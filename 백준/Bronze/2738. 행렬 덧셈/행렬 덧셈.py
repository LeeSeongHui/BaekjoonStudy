N,M = map(int, input().split())
A, B = [], []
for i in range(N):
    arr1 = list(map(int, input().split()))
    A.append(arr1)
for j in range(N):
    arr2 = list(map(int, input().split()))
    B.append(arr2)
for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=" ")
    print("")
