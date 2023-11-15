def solution(a, b):
    arr = []

    if a<= b:
        while a <= b:
            arr.append(a)
            a+=1
    else:
        while a >= b:
            arr.append(a)
            a-=1
            
    answer = sum(arr)
    return answer