# K_Flynn 05-04-2021
n = int(input())
array = list(map(int, input().strip().split()))[:n]
print(array)
q_1 = int(input())
q_2 = list(map(int, input().strip().split()))[:q_1]

for i in q_2:
    ano_arr = array[:i]
    print(min(ano_arr), max(ano_arr))

