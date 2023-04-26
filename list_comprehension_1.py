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

