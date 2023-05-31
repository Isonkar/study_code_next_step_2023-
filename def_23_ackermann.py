'''
Описать рекурсивную функцию ackermann, которая принимает на вход два целых числа  m и n находит значение, определенное следующим образом:



Найденное значение функция ackermann должна вернуть в качестве результата

ackermann(3, 2) => 29
ackermann(3, 0) => 5
ackermann(1, 0) => 2
ackermann(3, 5) => 253
Ваша задача только написать определение функции ackermann

В тестовых примерах сперва поступает на вход значение аргумента m, затем аргумента n.
'''

def ackermann(k: int, n: int) -> int:
    if k ==0: return n + 1
    if k > 0 and n == 0: return ackermann(k - 1, 1) 
    if k > 0 and n > 0: return ackermann(k - 1, ackermann(k, n -1)) 

k, n = int(input()), int(input())
print(ackermann(k, n))
