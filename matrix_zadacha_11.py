'''
Заполнение змейкой
Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой (см. пример).

Входные данные
Программа получает на вход два числа n и m.
Выходные данные
Программа должна вывести  полученный массив, при этом между числами может быть любое количество пробелов.

Sample Input 1:
4 10
Sample Output 1:
0  1  2  3  4  5  6  7  8  9
19 18 17 16 15 14 13 12 11 10
20 21 22 23 24 25 26 27 28 29
39 38 37 36 35 34 33 32 31 30

Sample Input 2:
3 4
Sample Output 2:
0 1 2 3 
7 6 5 4 
8 9 10 11
'''

n, m = map(int, input().split())
mat = [[0 for _ in range(m)] for _ in range(n)]
k = 0
for i in range(n):
    if i % 2 == 0:
       for j in range(m):
           mat[i][j] = k
           k += 1
    else:
        for j in range(-1, -m -1, -1):
            mat[i][j] = k
            k += 1          
for row in mat:
    print(*row)
    
# вариант два
n, m = map(int, input().split())

for i in range(n):
    if i % 2 == 0:
        print(*list(range(i * m, i * m + m)))
    else:
        print(*list(range(i * m, i * m + m))[::-1])
        
 # вариант три
n, m=map(int, input().split())
for i in range(n):
    a=[j for j in range(m*i, m+m*i)]
    if i%2 !=0:
        a.reverse()
    print(*a) 
    
 # вариант четыре
