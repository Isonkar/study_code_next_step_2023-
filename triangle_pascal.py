'''
треугольник имеет следующий вид, подробная лекция в разделе 5.8
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 



'''

n = int(input('Введите размер матрицы: '))
triangle = []

for i in range(n+1):
    triangle.append([1] + [0]*n)

for i in range(1, n+1):
    for j in range(1, i+1):
        triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]

for i in range(0, n+1):
    for j in range(0, i+1):
        print(triangle[i][j], end=" ")
    print()
    
    #поэтапно
    
    n = int(input('Введите размер матрицы: '))
triangle = []

for i in range(n+1):
    triangle.append([1] + [0]*n)

for i in triangle:
    print(i)
    
    
 '''
[1, 0, 0, 0, 0]
[1, 0, 0, 0, 0]
[1, 0, 0, 0, 0]
[1, 0, 0, 0, 0]
[1, 0, 0, 0, 0]
 '''
    
    
    
    
