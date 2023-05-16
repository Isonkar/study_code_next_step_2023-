'''
Напишите функцию factorial, которая принимает на вход одно неотрицательное число, и возвращает значение факториала данного числа.

Нужно написать только определение функции factorial

factorial(3) => 6
factorial(1) => 1
factorial(0) => 1
factorial(5) => 120

# знак => обозначает return
'''

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact
