'''Программа получает на вход натуральное число N. 
Нужно найти сумму его делителей. 
Sample Input 1:
10
Sample Output 1:
18'''

n = int(input())
i = n
res = []
while i > 0:
    if n % i == 0:
        res.append(i)
        i -= 1
        continue
    else:
        i -= 1
        continue
       
print(sum(res))
