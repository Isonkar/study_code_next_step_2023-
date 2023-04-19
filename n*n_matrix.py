'''Квадратная матрица
Очень часто вы будете иметь дело именно с квадратными таблицами, т.е. размерностью n на n.
В таких таблицах имеется главная диагональ, которая идёт из элемента [0][0] по пути [1][1], [2][2] и так до элемента [n][n]. 
Следовательно, у элементов главной диагонали номер строки совпадает с номером столбца, т.е. [i] = [j]
 
Эта диагональ делит матрицу на 2 треугольника. Первый треугольник состоит из элементов, расположенных выше главной диагонали: 
с элементами по индексу [0][1], [0][2], [1][2]. Второй треугольник с элементами по индексу [1][0], [2][0], [2][1].
В этих треугольниках наблюдается одна особенность:
У верхнего треугольника i < j, т.е. номер строки меньше номера столбца, а у нижнего треугольника i > j, т.е. номер строки больше номера столбца.
Теперь рассмотрим следующий пример: на главной диагонали будут лежать 10, ниже будут 3, а выше – 5.
Для этого сначала заполним матрицу нулями и проверим правильность заполнения:'''

a = []
n = int(input('Введите размер квадратной матрицы: '))
for i in range(n):
    a.append([0]*n)
for i in a:
    print(i)
    
    
# Как мы видим, всё работает исправно. Теперь чтобы изменить значения в этой таблице необходимо обходить их по индексам:
a = []
n = int(input('Введите размер квадратной матрицы: '))
for i in range(n):
    a.append([0]*n)
    
for i in range(n):
    for j in range(n):
        if i==j:
            a[i][j] = 10
        elif i>j:
            a[i][j] = 3
        else:
            a[i][j] = 5
for i in a:
    print(i)
