arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N,B = map(int,input().split())
answer = ''

while N != 0:
    answer += str(arr[N % B])
    N //= B
print(answer[::-1])