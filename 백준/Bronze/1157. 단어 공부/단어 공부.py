S = input().upper()
arr = list(set(S))
arr_c = arr.copy()

for i in arr:
    x = arr.index(i)
    arr[x] = S.count(i)

if arr.count(max(arr)) > 1:
    print("?")
else:
    print(''.join(arr_c[arr.index(max(arr))]))