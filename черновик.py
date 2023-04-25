n, m = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]


for i in range(1, n - 1):
    for j in range(1, m - 1):
        mat[i,j] = mat[i - 1][j] + mat[i - 1][j - 1]

for row in mat:
    print(*row)
