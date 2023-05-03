'''
Хранение данных об объектах
'''
'''
В этом словаре ключи – имена известных людей, а значения – словари. Внутри каждого из значений находятся одинаковые ключи: 
день рождения, город, телефон, количество детей. Это означает, что наш словарь contacts хранит соответствующую информацию о каждом человеке.
Создадим список с именами людей, которые находятся в нашем словаре и обойдем этим имена при помощи цикла for и получим для каждого имени контактную информацию:
'''

contacts = {
    'John Kennedy': {
        'birthday': '29 may 1917', 'city': 'Brookline',
        'phone': None, 'children': 3
    },
    'Arnold Schwarzenegger': {
        'birthday': '30 july 1947', 'city': 'Gradec',
        'phone': 555-555-555, 'children': 5
    },
    'Donald John Trump': {
        'birthday': '14 july 1946', 'city': 'New York',
        'phone': 777-777-777, 'children': 4
    }
}


persons = ['John Kennedy', 'Arnold Schwarzenegger', 'Donald John Trump']

for person in persons:
    print(person, contacts[person])
    print('-'*15)
print('/'*25)
for person in persons:
    print(person, contacts[person]['birthday'])
    
'''
Но поскольку вся эта контактная информация также является словарём мы можем достать из неё значения по соответствующему ключу, к примеру вывести только имя и день рождения:

for person in persons:
    print(person, contacts[person]['birthday'])
Также у нас есть возможность с помощью цикла for так сказать достать все эти данные и создать для них переменные:

persons = ['John Kennedy', 'Arnold Schwarzenegger', 'Donald John Trump']
for person in persons:
    birthday = contacts[person]['birthday']
    city = contacts[person]['city']
    phone = contacts[person]['phone']
    children = contacts[person]['children']
    print(person,  city, birthday)
'''


contacts = {
    'John Kennedy': {
        'birthday': '29 may 1917', 'city': 'Brookline',
        'phone': None, 'children': 3
    },
    'Arnold Schwarzenegger': {
        'birthday': '30 july 1947', 'city': 'Gradec',
        'phone': 555-555-555, 'children': 5
    },
    'Donald John Trump': {
        'birthday': '14 july 1946', 'city': 'New York',
        'phone': 777-777-777, 'children': 4
    }
}

persons = ['John Kennedy', 'Arnold Schwarzenegger', 'Donald John Trump']
for person in persons:
    print('-'*15)
    print(person)
    for data in contacts[person]:
        print(data, contacts[person][data])
        
        
 '''
 John Kennedy
birthday 29 may 1917
city Brookline
phone None
children 3
---------------
Arnold Schwarzenegger
birthday 30 july 1947
city Gradec
phone -555
children 5
---------------
Donald John Trump
birthday 14 july 1946
city New York
phone -777
children 4
 '''

