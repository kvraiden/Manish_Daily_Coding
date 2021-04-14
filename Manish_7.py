# K_Flynn
# 14-04-2021
# Beautiful Matrix

mat = []

x = y = 0

for i in range(5):
    matrix = input().split()
    mat.append(matrix)
    for j in range(0, 5):
        if(mat[i][j] == "1"):
            x = 3-i
            y = 3-j

print(abs(x) + abs(y))
