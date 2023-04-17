'''Давайте на практике применим метод подсчета

На вход вашей программе поступает положительное целое число n, а ваша задача вывести в порядке возрастания все цифры, которые встречались в этом числе,
и напротив каждого также необходимо вывести сколько раз данная цифра встречалась в числе n

Sample Input 1:
45654

Sample Output 1:
4 2
5 2
6 1
'''


a = [int(i) for i in input()]
count = [0] * (max(a) + 1)  #длина списка должна соответствовать максимальному элементу + 1
for i in a:
    count[i] += 1
for i in range(max(a) + 1):
    if count[i] > 0:        #данной проверкой не печатаем элементы с нудевым значением
        print(i, count[i])

        
#универсальный вариант   

n = list(input())
minimum = min(map(int, n))
maximum = max(map(int, n))
count = [0] * (maximum - minimum + 1)
for i in n:
    count[int(i) - minimum] += 1
for i in range(len(count)):
    if count[i] != 0:
        print(i + minimum, count[i])
