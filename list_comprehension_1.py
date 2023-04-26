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


