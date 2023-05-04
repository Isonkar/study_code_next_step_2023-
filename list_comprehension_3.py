'''
Разберём ещё один пример. У нас имеется строка, состоящая из различных символов, в которые входят буквы и цифры.
Мы можем при помощи генератора списка сформировать два списка: в одном будут хранится только цифры, в другом - только буквы
'''

s = 'gfdogjdf45i398gry74y543hgkgreiuYIUGd'
str_digits = [i for i in s if i.isdigit()]
print(str_digits)
print('-'*30)

int_digits = [int(i) for i in str_digits if i.isdigit()]
print(int_digits)

print('-'*30)
letters = [i for i in s if i.isalpha()]
print(letters)

