'''
Мы уже с вами подсчитывали сколько раз встречается число в списке при помощи метода подсчета. 
Там мы использовали список для хранения найденного количества

Теперь ваша задача научиться использовать словарь для подсчета количества. 
Вашей программе поступает на вход строка, вам необходимо подсчитать сколько раз встретилась каждая буква в этой строке без учета регистра, 
при этом цифры и символы пунктуации нужно пропустить. Ответ нужно сохранить в словаре, в котором ключ - буква, а значение - количество раз, 
сколько эта буква встретилась в строке. В качестве ответа нужно вывести словарь

Sample Input 1:
aabbbc
Sample Output 1:
{'a': 2, 'b': 3, 'c': 1}

Sample Input 2:
ZZzzzZ34 WWw777
Sample Output 2:
{'z': 6, 'w': 3}
'''
string = input().lower()
res_dict = {}
for i in range(len(string)):
    if string[i].isalpha():
        if res_dict.get(string[i], 0) == 0:
            res_dict[string[i]] = 1
        else:
            res_dict[string[i]] = res_dict.get(string[i]) + 1
print(res_dict)

#  вариант два
s = input().lower()
d = {i: s.count(i) for i in s if i.isalpha()}
print(d)

#  вариант три (с использованием коллекций)
from collections import Counter

print(dict(Counter(filter(str.isalpha, input().lower()))))
