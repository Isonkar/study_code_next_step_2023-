'''Проверьте, является ли двумерный массив симметричным относительно главной диагонали. 
Главная диагональ — та, которая идёт из левого верхнего угла двумерного массива в правый нижний.
Программа получает на вход число n<100, являющееся числом строк и столбцов в массиве. 
Далее во входном потоке идет n строк по n чисел, являющихся элементами массива.

Программа должна выводить слово Yes для симметричного массива и слово No для несимметричного.

Sample Input 1:
3
0 1 2
1 5 3
2 3 4
Sample Output 1:
Yes
Sample Input 2:
3
0 0 0
0 0 0
1 0 0
Sample Output 2:
No
'''

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
sum_row = 0
lst1 = []
lst2 = []
for i in range(n):
    for j in range(-1, i - n , -1):
        lst1.append(matrix[i][j])          
for i in range(n):
    for j in range(-1, i - n , -1):
        lst2.append(matrix[j][i])   
print('Yes' if lst1 - lst2 == 0 else 'No')


#вариант два(сократил один цикл)
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
lst1 = []
lst2 = []
for i in range(n):
    for j in range(-1, i - n , -1):
        lst1.append(matrix[i][j])          
        lst2.append(matrix[j][i])
print('Yes' if sum(lst1) - sum(lst2) == 0 else 'No')

#вариант три(оптимизация кода, с использованием конструкции break for else)
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(-1, i - n , -1):
        if matrix[i][j] != matrix[j][i]:
            print('No')
            break
    break       
else:
    print('Yes')


