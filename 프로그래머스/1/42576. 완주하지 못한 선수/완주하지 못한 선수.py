def solution(participant, completion):
    # (1) 효율성x
    # for i in completion:
    #     participant.remove(i)
    # return ' '.join(participant)
    
    #(2)
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]
    return participant[-1]
    
    