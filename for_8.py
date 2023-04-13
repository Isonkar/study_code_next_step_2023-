'''На вход программе поступает список из целых чисел. Ваша задача найти в данном списке наименьшее положительное значение. 
В случае, если положительных значений нет, выведите строку "Empty"

Sample Input 1:
8 11 -9 0 5 -20

Sample Output 1:
5
'''

lst = list(map(int, input().split()))
lst.sort()
result_lst = []
for n in lst:
    if n > 0:
        result_lst.append(n)
print(result_lst[0] if len(result_lst) > 0 else 'Empty')
