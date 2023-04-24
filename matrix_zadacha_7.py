'''Заполнение матрицы
Ваша задача сформировать квадратную матрицу размером NxN, в которой используется следующее заполнение:

все элементы, находящиеся выше главной диагонали, заполняются значением A;
все элементы, находящиеся ниже главной диагонали, заполняются значением B;
все элементы, находящиеся на главной диагонали, заполняются значением C.
В качестве ответа, выведите на экран полученную матрицу

Входные данные
Программа сперва принимает на вход число N (N<=15) - количество строк и столбцов в матрицы, а затем на новой строке три целых числа  A, B и C. 
Данные числа используются для заполнения

Выходные данные
Заполните и распечатайте матрицу

Sample Input 1:

3
1 0 3
Sample Output 1:

3 1 1
0 3 1
0 0 3
'''

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
            mat[j][i] = lst[2]

for i in mat:
    print(*i)
    
    
    
#вариант два

n = int(input())
A, B, C = map(int, input().split())
tab = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            tab[i][j] = C
        elif i < j:
            tab[i][j] = A
        elif i > j:
            tab[i][j] = B
for i in tab:
    print(*i)
    
#вариант три

n, values = int(input()), input().split()
[print(*[values[(i == j) + (i <= j)] for i in range(n)]) for j in range(n)]
