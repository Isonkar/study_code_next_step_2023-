'''
Вашей программе будут поступать на вход N списков, содержащих целые числа
Ваша задача определить сколько всего встречалось различных чисел во всех этих списках

Входные данные
Сперва поступает натуральное число N - количество списков
В следующих N строк вводятся значения каждого списка, разделенные через пробел
Выходные данные
Вывести одно число - количество различных чисел во всех этих списках

Sample Input 1:
2
1 2 3 2 1 4
1 1 2 2 2

Sample Output 1:
4
'''

matrix = [{int(i) for i in input().split() if i.isdigit()} for _ in range(int(input()))]
res_set = matrix[0]
for i in range(len(matrix) - 1):
    res_set =  res_set | matrix[i + 1] 
   
print(len(res_set))

# вариант два
a = set()
{a.update(input().split()) for word in range(int(input()))}
print(len(a))
