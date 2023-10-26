for _ in range(int(input())):
    C = int(input())
    for i in [25,10,5,1]:
        print(C // i, end=' ')
        C %= i
    print()