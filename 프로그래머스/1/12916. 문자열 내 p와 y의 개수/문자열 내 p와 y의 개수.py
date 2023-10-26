def solution(s):
    answer = True
    S = s.upper()

    if S.count('P') == S.count('Y'):
        return answer
    else:
        return False