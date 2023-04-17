'''Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

Пример выходного файла:
ff
dde
c
ab'''


lst =[]
with open('in.txt') as in_file, open('out.txt',"w") as out:
    for line in in_file:
        line = line.strip()
        lst.append(line)
    lst = lst[::-1]
    for elem in lst:
        out.write(elem + '\n')
