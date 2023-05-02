'''
Переменные countries соединяют ряд стран с тремя крупнейшими городами каждой страны. 

Программе на вход будет поступать название города в переменную city. И ваша задача найти какой стране принадлежит введенный город.
Если страна успешно найдена, необходимо вывести сообщение:

INFO: <City> is a city in <Country>
в противном случае
ERROR: Country for {City} not found
Учитывайте, что регистр букв имеет значение

Sample Input 1:
Birmingham
Sample Output 1:
INFO: Birmingham is a city in England
Sample Input 2:
Moscow
Sample Output 2:
ERROR: Country for Moscow not found
'''

countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()
flag = 0
for key, value in countries.items():
    if city in value:
        print(f'INFO: {city} is a city in {key}')
        flag = 1

if flag == 0:
    print(f'ERROR: Country for {city} not found')
    
#  вариант два 

city = input()
for key, value in countries.items():
    if city in value:
        print(f'INFO: {city} is a city in {key}')
        break

else:
    print(f'ERROR: Country for {city} not found')
