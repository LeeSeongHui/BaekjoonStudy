def solution(s):
    
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else: # i == ')'인 경우
            if stack == []: # ')'로 시작하면 안됨
                return False
            else:
                stack.pop() # stack의 '('가 ')'와 짝을 이루게될경우
    
    return stack==[]