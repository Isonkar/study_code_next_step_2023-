n = int(input())
lst = list(map(int, input().split()))

mat = [[i * 0  for i in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        mat[i][j] = lst[0]

for i in range(n):
    for j in range(i + 1, n):
        mat[j][i] = lst[1]


for i in range(n):
    for j in range(n):
      if i == j:  
          mat[j][i] = lst[3]



for i in mat:
    print(*i)
