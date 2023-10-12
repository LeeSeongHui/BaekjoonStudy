chk = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

S = input()
for i in chk:
    S = S.replace(i,'*')
print(len(S))