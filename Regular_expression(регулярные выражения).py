import re

# print(re.match())  # берет шаблон и строку и проверяет подходит ли строка под шаблон
# print(re.search())   # берет нашу строку и находит первую подстроку которая подходит под шаблон
# print(re.findall())  # как серч, только находит все подстроки
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
''' 
\d подходят все цифры (0-9)
\D не подходят цифры
\s  подходит все пробельные символы
\S не подходит все пробельные символы
\w все буквы + цифры + _
\W не подходит
'''
