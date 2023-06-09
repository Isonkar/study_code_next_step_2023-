'''
Пользуясь вложенными функциями, реализуйте простой калькулятор.
Необходимо реализовать функцию calculate , которая принимает три параметра:

обязательный числовой параметр x
обязательный числовой параметр y
необязательный строковый параметр operation,  по умолчанию принимает значение английской буквы a
В данной функции должны быть реализованы следующие функции:

addition - печатаем сложение двух чисел,
subtraction - печатаем вычитание из первого переданного параметра второго;
division - печатаем деление первого на второго,
multiplication - печатаем умножение двух чисел.
Каждая из этих четырёх вложенных функций должна распечатать результат математической операции и ничего не возвращать

А при помощи параметра operation и условного оператора нужно выбрать какая из функций должна быть вызвана:

если operation = a, вызываем функцию addition;
если operation = s, вызываем функции subtraction;
если operation = d, вызываем функции division;
если operation = m, вызываем функции multiplication;
calculate(2, 5) # Печатает 7.0
calculate(2.2, 15, 'a') # Печатает 17.2
calculate(22, 15, 's') # Печатает 7.0
calculate(2, 3.2, 'm') # Печатает 6.4
calculate(10, 0.4, 'd') # Печатает 25.0
 

Если operation принимает значение, отличное от перечисленных выше букв, то необходимо вывести на экран  сообщение Ошибка. Данной операции не существует.
Также если мы выполняем деление, то второе число (y) не должен равняться нулю, в противном случае необходимо вывести на экран: На ноль делить нельзя!

Sample Input 1:

10
4
s
Sample Output 1:

6.0
'''

def calculate(x:float, y:float, operation:str='a') -> None:
    def addition(x, y):
      print(x + y)

    def division(x, y):
      if y == 0: print('На ноль делить нельзя!')
      else: print(x / y)

    def subtraction(x, y):
      print(x - y)

    def multiplication(x, y):
      print(x * y)

    if operation == 'a': addition(x, y)
    if operation == 's': subtraction(x, y)
    if operation == 'd': division(x, y)
    if operation == 'm': multiplication(x, y)
    if operation not in ['m', 'd', 's', 'a']: print('Ошибка.')


calculate(float(input()), float(input()), input())
