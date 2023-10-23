# 세로읽기

# 한 문장식 저장
words = []
for _ in range(5):
    word = input()
    words.append(word)

# 세로로 읽어서 출력. 단, 해당 단어에 글자가 남아있을때 출력
for i in range(15):
    for j in range(5):
        if len(words[j]) > i:
            print(words[j][i], end="")