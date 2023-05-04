'''
Декартово произведение
Декартово произведение двух множеств — множество, элементами которого являются все возможные упорядоченные пары элементов исходных множеств. 
Под множествами в этой задачи мы будем считать списки, один из них будет содержать цвета маек, а другой размеры одежды. 

Если объяснять более простым языком, то  декартово произведение это когда вы каждый элемент из одного множества группируете с каждый элементом другого множества. 
Например, если бы у вас имелись такие списки 

colors = ['red', 'green']
sizes = ['S', 'M', 'L']
то их декартово произведение выглядело бы так

[('red', 'S'), ('red', 'M'), ('red', 'L'), ('green', 'S'), ('green', 'M'), ('green', 'L')]
Здесь мы берем каждый цвет и сочетаем его с каждым размером. Общее количество элементов в данном декартовом множестве рассчитывается по формуле

len(colors) * len(sizes)
Ваша задача создать список кортежей на основании переменных colors и sizes. 

Обратите внимание на порядок элементов в ответе, сперва мы берем первый цвет и для него перебираем все возможные размеры. Порядок формирования в этом задании важен

В качестве ответа выведите на экран полученный список кортежей

Sample Input:

Sample Output:

[('White', 'S'), ('White', 'M'), ('White', 'L'), ('White', 'XL'), ('White', 'XLL'), ('Blue', 'S'), 
('Blue', 'M'), ('Blue', 'L'), ('Blue', 'XL'), ('Blue', 'XLL'), ('Yellow', 'S'), ('Yellow', 'M'), 
('Yellow', 'L'), ('Yellow', 'XL'), ('Yellow', 'XLL'), ('Purple', 'S'), ('Purple', 'M'), ('Purple', 'L'), 
('Purple', 'XL'), ('Purple', 'XLL'), ('Black', 'S'), ('Black', 'M'), ('Black', 'L'), ('Black', 'XL'), ('Black', 'XLL'), ('Green', 'S'),
('Green', 'M'), ('Green', 'L'), ('Green', 'XL'), ('Green', 'XLL')]
'''

colors = ['White', 'Blue', 'Yellow', 'Purple', 'Black', 'Green']
sizes = ['S', 'M', 'L', 'XL', 'XLL']
print([(colors[j], sizes[i]) for j in range(len(colors)) for i in range(len(sizes))])

#  var 2
from itertools import product as decart

print(list(decart(colors, sizes)))
