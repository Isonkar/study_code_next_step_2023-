'''
Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.

Сложным паролем будет считаться комбинация символов, в которой :
Есть хотя бы 3 цифры
Есть хотя бы одна заглавная буква 
Есть хотя бы один символ из следующего набора "!@#$%*"
Общая длина не менее 10 символов
Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy"

Вам необходимо написать только определение функции check_password
Разбор Youtube Patreon Boosty
Sample Input 1:
qwerty
Sample Output 1:
Easy peasy
Sample Input 2:
Qwerty1357!
Sample Output 2:
Perfect password
'''

def check_len(password):
    if len(password) >= 10: return True

def check_symbol(password):
    for i in password:
        if i in '!@#$%*':
            return True

def check_digit(password):
    count = 0
    for i in password:
        if i.isdigit():
            count += 1
    if count >= 3: return True

def check_upper(password):
    for i in password:
        if i.isupper():
            return True

def check_password(password):
    print('Perfect password' if (check_digit(password) and check_len(password) and check_symbol(password) and check_upper(password)) else 'Easy peasy')
    
# var 2 regular exp
import re
def check_password(n):
    rule1 = len(re.findall("\d",n))>=3
    rule2 = bool(re.search("[A-Z]",n))
    rule3 = bool(re.search("[!@#$%*]",n))
    rule4 = len(n)>=10
    if rule1 and rule2 and rule3 and rule4:
        print('Pefrect password')
    else: print('Easy peasy')
      
 # var 3 
