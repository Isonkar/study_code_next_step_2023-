'''Как видно из названия задачи, вам необходимо отсортировать список, состоящий только из чисел в пределах от -100 до 100 включительно, сортировкой подсчетом.
Программа получает на вход число n - количество элементов в списке, затем сами элементы списка
Вам необходимо вывести отсортированный список
P.S. не пользуйтесь встроенной функцией sorted или методом sort

Sample Input 1:
5
8 9 8 7 2
'''

n = int(input())
lst = list(map(int, input().split()))
minimum = min(lst)
maximum = max(lst)

count = [0] * (maximum - minimum + 1)
for i in lst:
    count[i - minimum] += 1
for i in range((maximum - minimum) + 1):
    if count[i] > 0:
        print((str(i + minimum) + ' ') * count[i], end='')
