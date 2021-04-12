# K_Flynn
# 06-04-2021
fans = []


def addtwo():
    ab = list(map(int, input().strip().split()))
    fans.append(sum(ab))


n = int(input())
while n > 0:
    addtwo()
    n -= 1

for ele in fans:
    print(ele)
