'''
Напишите функцию first_unique_char, которая принимает строку символов и возвращает целое число: позицию первого уникального символа в строке. 
В случае, если уникальных символов в переданной строке нет, верните -1. Регистр символов не учитывайте.
Ваша задача написать только определение функции first_unique_char

Sample Input 1:

python
Sample Output 1:

0
Sample Input 2:

abracadabra
Sample Output 2:

4
'''

def first_unique_char(s):
    for char in s:
        if s.count(char) == 1:
            return s.index(char)
        else:
            continue
    else:
        return -1


s = input()
print(first_unique_char(s))

# var 2
def first_unique_char(s):    
    for i in s:            
        if s.count(i) == 1 and s.count(i) < 2:
            return s.index(i)
    return -1
