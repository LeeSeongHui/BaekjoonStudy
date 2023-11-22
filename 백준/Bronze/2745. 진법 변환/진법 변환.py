answer = 0
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N,B = input().split()

N_reverse = N[::-1]
for i,n in enumerate(N_reverse):
    answer += (int(B)**i)*arr.index(n)
print(answer)