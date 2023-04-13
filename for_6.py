'''Входные данные
На первой строке вводится один символ — строчная буква.
На второй строке вводится предложение.

Выходные данные
Нужно вывести список слов (словом считается часть предложения, окружённая символами пустого пространства), в которых присутствует введённая буква в любом регистре, в том же порядке, в каком они встречаются в предложении.
Sample Input 1:
a
Mary had a little lamb.
Sample Output 1:
Mary
had
a
lamb.'''


split_ = input()
lst = list(map(str, input().split()))

for word in lst:
    if split_.lower() in word.lower():
        print(word, end = '\n')
        
 #вариант второй
letter = input()
print(*[i for i in input().split() if letter in i], sep='\n')
        
        
