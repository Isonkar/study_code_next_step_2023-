'''
А теперь попробуем при помощи генератора обработать данные, которые хранятся в словаре. Пусть у нас будет такой вложенный словарь:
Рассмотрим один из его элементов: ключом является фамилия человека, а значением является словарь, состоящий из 3 ключей: возраст, хобби, автомобиль. 
Давайте получим какие-то данные при помощи генератора.
'''

a = {
    'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
    'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
    'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
    'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
    'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
    'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
    'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
    'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
}
cars = [a[elem]['car'] for elem in a]
print(cars)
print('-'*30)
hobbies = [a[elem]['hobby'] for elem in a]
print(hobbies)
print('-'*30)
cars_lt_2000 = [a[elem]['car'] for elem in a if a[elem]['age'] < 2000]
print(cars_lt_2000)
print('-'*30)
name_with_car = [(elem, a[elem]['car']) for elem in a 
                        if a[elem]['age'] < 2000]
print(name_with_car)
print('-'*30)
less_2000_and_soccer = [(elem, a[elem]['car']) for elem in a 
         if a[elem]['age'] < 2000 and a[elem]['hobby'] == 'soccer'] 
print(less_2000_and_soccer)

'''
В итоге, мы получили список из ключей (в нашем случае фамилий) и список словарей. 
Поскольку мы получаем словарь, то мы можем по двойной индексации обратиться к какому-либо значению вложенного словаря. 
Например, получим список, состоящий из

машин владельцев
хобби владельцев
машин, владельцы которых родились раньше 2000
из кортежей (имя владельца, машина), где год рождения меньше 2000
из кортежей (имя владельца, машина), где год рождения меньше 2000 и хобби футбол
'''
