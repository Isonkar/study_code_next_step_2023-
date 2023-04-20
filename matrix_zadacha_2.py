'''Состязания - 3
В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Побеждает спортсмен, у которого максимален наилучший бросок. 
Если таких несколько, то из них побеждает тот, у которого наилучшая сумма результатов по всем попыткам. 
Если и таких несколько, победителем считается спортсмен с минимальным номером. Определите номер победителя соревнований.

Входные данные
Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. 
Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.

Выходные данные
Программа должна вывести одно число - номер победителя соревнований. Не забудьте, что  строки  (спортсмены) нумеруются с 0.



Sample Input 1:
3 3
1 2 7
1 3 5
4 1 6
Sample Output 1:
0

Sample Input 2:
2 3
1 2 7
1 7 5
Sample Output 2:
1
'''

a, b = map(int, input().split())
winner = 0
max_in_line = 0
max_sum_in_line = 0

m = [list(map(int, input().split())) for _ in range(a)]
for i in range(a):
    for j in range(b):
        if m[i][j] > max_in_line:
            winner = i
            max_in_line = m[i][j]
            max_sum_in_line = sum(m[i])
        elif m[i][j] == max_in_line:
            if sum(m[i]) > max_sum_in_line:
                winner = i
                max_sum_in_line = sum(m[i])
            
print(winner)
