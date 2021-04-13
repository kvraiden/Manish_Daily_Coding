t = int(input())
ans = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans.append(sum(a))

print('\n'.join(map(str, ans)))
