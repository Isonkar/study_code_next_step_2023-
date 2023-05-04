'''
Также вы можете спокойно обходить элементы матрицы внутри генератора списка по значениям, 
для этого достаточно во внутреннем цикле обращаться к итерируемой переменной внешнего цикла
'''

from random import randint
n = 3
m = 4
matrix = [[randint(1,10) for j in range(m)] for i in range(n)]
for current_row in matrix:
    print(current_row)
    
print('-'*30)

squares = [num**2 for row in matrix for num in row]
print(squares)

'''
[8, 3, 10, 8]
[9, 7, 10, 6]
[1, 9, 9, 2]
------------------------------
[64, 9, 100, 64, 81, 49, 100, 36, 1, 81, 81, 4]
 

'''
