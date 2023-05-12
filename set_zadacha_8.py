'''
Напишите программу, которая выводит все цифры, встречающиеся в символьной строке больше одного раза.

Входные данные
Входная строка может содержать содержит цифры, пробелы и латинские буквы.
Выходные данные
Программа должна вывести в одну строчку в порядке возрастания все цифры, встречающиеся во входной строке больше одного раза. 
Если таких цифр нет, нужно вывести слово 'NO'.

Sample Input 1:
abc12cd34ef35
Sample Output 1:
3

Sample Input 2:
yrey424u3iou2315
Sample Output 2:
2 3 4
'''

string = input()
my_set = set()
for i in string:
    if i.isdigit() and string.count(i) > 1:
        my_set.add(i)

if len(my_set) > 0:
    print(*sorted(my_set))
else:
    print('NO')

#  вариант два
s = input()
print(*sorted(set(i for i in s if i.isdigit() and s.count(i) > 1)) or ['NO'])
