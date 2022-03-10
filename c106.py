# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
scores = [int(x) for x in input().split()]
index = [i+1 for i in range(N)]

scores, index = zip(*sorted(zip(scores, index), reverse = True))

medal = []
pattern = 0
for i in range(1,N+1):
    if pattern == 1:
        for j in range(N-len(medal)):
                medal.append("N")
        break
    else:
        if i == 1:
            l=scores.count(sorted(scores)[-i])
            for j in range(l):
                medal.append("G")
        elif i == 2:
            l=scores.count(sorted(scores)[-i])
            if len(medal)>1:
                continue
            for j in range(l):
                medal.append("S")
        elif i == 3:
            l=scores.count(sorted(scores)[-i])
            if len(medal)>2:
                pattern=1
                continue
            for j in range(l):
                medal.append("B")
            pattern = 1


index, medal = zip(*sorted(zip(index, medal), reverse = True))

for j in reversed(list(medal)):
    print(j)
