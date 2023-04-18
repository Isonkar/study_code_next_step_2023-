'''Напишите программу для построения горизонтальных столбчатых диаграмм с помощью символа звёздочки. 
Формат ввода
Несколько натуральных чисел на одной строке.
Формат вывода
Несколько чисел на одной строке.
Sample Input:
3 7 1 10 8
Sample Output:
***
*******
*
**********
********
'''
lst_n = list(map(int, input().split()))
[print('*' * lst_n[i], end='\n') for i in range(len(lst_n))]

# for i in range(len(lst_n)):
#     print('*' * lst_n[i], end='\n')

#[print('*' * i, sep='\n') for i in map(int, input().split())]
