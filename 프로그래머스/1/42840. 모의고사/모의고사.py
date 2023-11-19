def solution(answers):
    answer = []
    chk = [0,0,0]
    
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == one[i%5]:
            chk[0] += 1
        if answers[i] == two[i%8]:
            chk[1] += 1
        if answers[i] == three[i%10]:
            chk[2] += 1
    
    for idx, num in enumerate(chk):
        if num == max(chk): 
            answer.append(idx+1)
    return answer