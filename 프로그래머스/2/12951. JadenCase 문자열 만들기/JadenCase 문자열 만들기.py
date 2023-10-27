# def solution(s): 
#     seq = s.split(' ')
#     answer = []
#     for word in seq:
#         if word : 
#             answer.append(word[0].upper() + word[1:].lower())
#         else :
#             answer.append(word)
#     return ' '.join(answer)     
        
def solution(s):
    answer = []
    seq = s.split(' ')
    for word in seq:
        if word:
            answer.append(word[0].upper() + word[1:].lower())
        else:
            answer.append(word)
    return ' '.join(answer)  
