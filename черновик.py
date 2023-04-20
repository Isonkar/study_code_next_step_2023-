n,m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

res_dict = {}
winner = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > winner:      
            winner = matrix[i][j]
    res_dict[i] = [sum(matrix[i]), winner]
    winner = 0
