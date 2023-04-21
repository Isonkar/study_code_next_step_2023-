#теория
#_______________________________________________________________________________________________________________________________________________
import re
# print(re.match())  # берет шаблон и строку и проверяет подходит ли строка под шаблон
# print(re.search())   # берет нашу строку и находит первую подстроку которая подходит под шаблон
# print(re.findall())  # как серч, только находит все подстроки (данные выводит в формате списка)
# print(re.sub())      # замняет все вхождения чем нибудь другим
# pattern = r'abc'
# string = 'abc'
# match_object = re.search(pattern, string)
# print(match_object)
pattern = r'a[abc]c'
string = 'acc'
match_object = re.match(pattern, string)
print(match_object)

string = 'abc, acc, aac'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, 'abc', string) # если в строке стринг находим совпадения с паттерном, заменяем на значение 'abc
print(fixed_typos)
# мета символы . ^ $ * ? {} [] () \ | 
# [] -- указываем множество подходящик -- диапазон
# ^ означает не подходит
# ^ означает не подходит
# . подходит любой символ
# * подходит любое количество букв (например в* - подходит и в и вв и ввв и т.д)
# + больше нуля(положительные)
# ? - 0 или одно вхождение символа
# {} - указываем сколько вхождений нас интересует, например b{3} будет искать вхождение для bbb. если указать числа через запятую будет диапазон


''' 
\d подходят все цифры (0-9)
\D не подходят цифры
\s  подходит все пробельные символы
\S не подходит все пробельные символы
\w все буквы + цифры + _
\W не подходит
'''

'''
() метасимвол используется для группировки
| символ или
_________________________________________________________________________________________________________________________
'''
'''
_________________________________________________________________________________________________________________________
Задача 1:
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
Примечание:
Считать все строки по одной из стандартного потока ввода вы можете, например, так
import sys
for line in sys.stdin:
    line = line.rstrip()
    # process line

Sample Input:
catcat
cat and cat
catac
cat
ccaatt
Sample Output:
catcat
cat and cat
'''
import sys, re

pattern = r'cat'
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) > 1:
        print(line)

 # вариант два
import re
import sys
# Читаем строки из stdin и удаляем символы переноса строки в конце каждой строки
lines = [line.rstrip() for line in sys.stdin]
# Перебираем строки и выводим те, в которых "cat" встречается хотя бы два раза
for line in lines:
    matches = re.findall("cat", line)
    if len(matches) >= 2:
        print(line)
        
        
        
#________________________________________________________________________________________________________________________
'''
Задача 2:
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.
Примечание:
Для работы со словами используйте группы символов \b и \B.

Sample Input:
cat
catapult and cat
catcat
concat
Cat
"cat"
!cat?

Sample Output:
cat
catapult and cat
"cat"
!cat?
'''

import sys, re

pattern = r'\bcat\b'
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)):
        print(line)

# вариант два

import re
import sys

def search(line):
    if re.search(r'\bcat\b|\Bcat\B', line):
        print(line)
for line in sys.stdin:
    search(line.rstrip())

#_________________________________________________________________________________________________________________
'''
Задача 3
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z", между которыми ровно три символа.

Sample Input:
zabcz
zzz
zzxzz
zz
zxz
zzxzxxz

Sample Output:
zabcz
zzxzz
'''

import sys, re

pattern = r'z...z'
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) > 0:
        print(line)
        
# вариант два
import sys, re

pattern = r'z...z'
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line) != None:
        print(line)
        
#_____________________________________________________________________________________________________
'''Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

Sample Input:
blabla is a tandem repetition
123123 is good too
go go
aaa

Sample Output:
blabla is a tandem repetition
123123 is good too
'''

import sys, re

pattern = r'\b(\w+)\1\b'
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) > 0:
        print(line)
 
# вариант два

import sys, re

pattern = r"\b(\w+)\1\b"
for line in sys.stdin:
    line = line.rstrip()
    if (re.search(pattern, line)): print(line)
 
