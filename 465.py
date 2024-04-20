n, m = map(int, input().split())
a = [[0] * n for _ in range(n)]
for i in range(m):
    r, c = map(int, input().split())
    a[r-1][c-1] = a[c-1][r-1] = 1
for i in a:
    print(*i)
    

