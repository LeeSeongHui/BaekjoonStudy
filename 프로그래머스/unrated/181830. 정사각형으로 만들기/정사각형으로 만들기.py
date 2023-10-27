def solution(arr):
    answer = []
    if len(arr) > len(arr[0]):
        for x in arr:
            answer.append(x + [0]*(len(arr)-len(arr[0])))
    elif len(arr) < len(arr[0]):
        for _ in range(len(arr[0]) - len(arr)):
            arr.append(list([0]*len(arr[0])))
            answer = arr
    else :
        answer = arr
    return answer