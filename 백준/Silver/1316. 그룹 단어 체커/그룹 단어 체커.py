N = int(input())
cnt = N
for _ in range(N):
    S = list(input()) 
    chk = [S[0]]
    for i in range(len(S)-1):
        # 앞뒤 알파벳을 비교해서 같으면 계속검사, 다르면 체크리스트에 추가
        # 체크리스트 추가시 이미 있는 알파벳이면 cnt-1(그룹함수에서 제외)   
        if S[i] == S[i+1]:
            continue
        else:
            if S[i+1] not in chk:
                chk.append(S[i+1])
            else:
                cnt-=1 
                break    
print(cnt)