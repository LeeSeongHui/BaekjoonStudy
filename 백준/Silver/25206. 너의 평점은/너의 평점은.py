score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
total = 0
sum = 0
for _ in range(20):
    a,b,c = input().split()
    if c != 'P':
        sum += (float(b) * score[grade.index(c)])
        total += float(b)
print(sum/total)  