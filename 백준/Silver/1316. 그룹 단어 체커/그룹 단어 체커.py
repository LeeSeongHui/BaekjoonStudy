N = int(input())
cnt = N
for _ in range(N):
    S = list(input()) 
    chk = [S[0]]
    for i in range(len(S)-1): 
        if S[i] == S[i+1]:
            continue
        else:
            if S[i+1] not in chk:
                chk.append(S[i+1])
            else:
                cnt-=1 
                break   
print(cnt)