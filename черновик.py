n, x = map(int, input().split())
mat = [[1 * i for i in range(1, n + 1)] for _ in range(1, n + 1)]

cnt = 0
for i in range(1, n):
    for j in range(1, n):
        mat[i][j] = i * j
        if mat[i][j] == x:
            cnt +=1

for i in mat:
    print(i)
print(cnt)
        
