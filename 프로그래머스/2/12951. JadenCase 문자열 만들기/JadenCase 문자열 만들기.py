# def solution(s): 

#     seq = s.split()
#     print(seq)
#     answer = []
#     for word in seq:
#         if word[0].isalpha() == True : # 첫 문자가 알파벳일 떄
#             answer.append(word[0].upper() + word[1:].lower())
#         else :
#             answer.append(word[0] + word[1:].lower())
    
#     return ' '.join(answer)  


def solution(s):
    answer = []
    s = s.split(" ")
    for word in s:
        print(word)
        if word:
            answer.append(word[0].upper() + word[1:].lower())
        else:
            answer.append(word)
    return " ".join(answer)