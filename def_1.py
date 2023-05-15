'''
Напишите функцию sum_num для суммирования всех цифр строки.
Функция должна принимать строку, суммировать все ее символы, которые являются цифрами,
и в качестве ответа выводить найденную сумму.
Вам необходимо написать только определение функции sum_num .

Sample Input 1:
4
Sample Output 1:
4

Sample Input 2:
123QwertY321
Sample Output 2:
12
'''

def sum_num(string):
    print(sum([int(i) for i in string if i.isdigit()]))
    
#  var 2
