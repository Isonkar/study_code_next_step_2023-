'''
Наша программа принимает на вход последовательность скобочных символов. Ваша задача определить является ли введенная скобочная последовательность правильной.
Правильная скобочная последовательность (ПСП) называется строка, состоящая только из символов "скобки", где каждой закрывающей скобке найдётся
соответствующая открывающая (причём того же типа). При этом учитывайте, что:
Пустая последовательность является правильной.
Если A – правильная скобочная последовательность, то (A), [A] и {A} – правильные скобочные последовательности.
Если A и B – правильные скобочные последовательности, то AB – правильная скобочная последовательность.
Если введенная строка является ПСП, выведите YES, в противном случае - NO.

Разбор решения задачи
Sample Input 1:
[]
Sample Output 1:
YES
Sample Input 2:
[(])
Sample Output 2:
NO'''


string = input()

if string.count('(') != string.count(')') or string.count('[') != string.count(']') or string.count('{') != string.count('}'):
    print('NO')
elif any([ i for i in ('[)', '[}', '(]', '(}', '{]', '{)') if i in string]):
    print('NO')
        
else:
    print('YES')

# вариант второй (реплейс)
pattern = input()
for i in range(len(pattern) // 2):
    pattern = pattern.replace('{}', '')
    pattern = pattern.replace('()', '')
    pattern = pattern.replace('[]', '')
print('YES' if len(pattern) == 0 else 'NO')

# вариант три (СТЕКОВЫЙ)
s, match, stack = input(), {'[]', '{}', '()'}, ['-']
if len(s) % 2 != 0:
    print('NO')
else:    
    for c in s:
        if c in '[({':
            stack.append(c)
        elif (stack.pop() + c) not in match:
            print('NO')
            break
    else:
        print(('NO', 'YES')[stack[-1] == '-'])
