print([i for i in range(1, int(input()) + 1)])

'''
При помощи генератора-списка создайте список [1, 2, 3, ..., n], само натуральное число n будет поступать на вход вашей программе.
'''

n = int(input())
print([i for i in range(1, n + 1) if  n % i == 0])
#nex var
print([i for n in [int(input())] for i in range(1, n+1) if not n % i])
'''
На вход программе подается натуральное число n (n<=1000). При помощи list comprehension создайте список, состоящий из делителей введенного числа.
Sample Input 1:
4
Sample Output 1:
[1, 2, 4]
'''

n = int(input())
print([i for i in range(n, n*n +1) if i % 2 != 0])
'''
При помощи list comprehension создайте список, состоящий из нечетных натуральных чисел в интервале [ n; n*n] и вывести его на экран. Само число 
n поступает на вход программе

Sample Input 1:
7
Sample Output 1:
[7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
'''

a, b = map(int, input().split())
if a <= b:
    print([i ** 2 for i in range(a, b + 1)])
else:
    print(sorted([i ** 3 for i in range(b, a + 1)], reverse=True))

#вариант два (тоже но короче)
a, b = map(int, input().split())
print([i ** 2 for i in range(a, b + 1)] if a <= b else sorted([i ** 3 for i in range(b, a + 1)], reverse=True))

#вариант три
a, b = map(int, input().split())
print([i**2 for i in range(a, b + 1)] or [i**3 for i in range(a, b - 1, -1)]) 
# or идет как условие, условие заключено в логике ''or'', запустится один из 
# генераторов в зависимости от того,  какому условию range удовлетворят входные данные. 
# Например, итерация по range(a, b + 1) не запустится если a > b.

'''
Программа принимает на вход два целых числа a и b.
Если a<=b необходимо сформировать список квадратов целых чисел на интервале от а до b включительно и вывести его на экран.
Если же a>b, необходимо сформировать список кубов целых чисел на интервале от a до b включительно, двигаясь в порядке убывания, и затем вывести его.
Не забывайте пользоваться генератором списков 
Sample Input 1:
1 5
Sample Output 1:
[1, 4, 9, 16, 25]
Sample Input 2:
3 1
Sample Output 2:

[27, 8, 1]
'''
st = 'Create a list of the first letters of every word in this string'
print([i[0] for i in list(map(str, st.split()))])

'''
Создайте список первых букв каждого слова из строки st и выведите его на экран
st = 'Create a list of the first letters of every word in this string'
'''

from string import ascii_uppercase
print([i for i in ascii_uppercase[:int(input())]])
'''
При помощи list comprehension создайте список, состоящий из первых n заглавных букв английского алфавита ['A', 'B', 'C', 'D', ...]. 
Получить все заглавные буквы английского алфавита можно следующим образом:
from string import ascii_uppercase
print(ascii_uppercase) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ
Входные данные
На вход программе подается натуральное число n, n≤26.
Формат выходных данных
Программа должна вывести список из первых n заглавных букв английского алфавита
Sample Input 1:
3
Sample Output 1:
['A', 'B', 'C']
'''





