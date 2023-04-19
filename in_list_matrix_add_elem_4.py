'''добавляем нулевые значения в список
'''

a = []
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
for i in range(n):
    a.append([0]*m)
for i in a:
    print(i)
    
# заполняем массив произвольными данными  
a = []
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
for i in range(n):
    b = []
    for i in range(m): 
        b.append(int(input('Введите элемент: ')))
    a.append(b)
for i in a:
    print(i)
