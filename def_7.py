 '''
 
 Fizz Buzz  список
Напишите функцию generate_fizz_buzz_list, которая принимает одно целое число n - размер списка. Функция generate_fizz_buzz_list должна

обойти числа от 1 до n включительно и для каждого такого числа выполнить последовательно проверки с пункта 2 по пункт 5
Если число кратно и трем, и пяти, то в список заносим строку FizzBuzz 
Если число кратно трем, то в список заносим строку Fizz
Если число кратно пяти, то в список заносим строку Buzz
Если число не кратно ни трем ни пяти, то в список заносим само это число
В итоге функция generate_fizz_buzz_list должна вернуть сформированный список из n элементов. Ниже показаны примеры вызова:

generate_fizz_buzz_list(3)  => [1, 2, 'Fizz']
generate_fizz_buzz_list(7)  => [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7]
generate_fizz_buzz_list(15) => [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
Ваша задача написать только определение функции generate_fizz_buzz_list

Sample Input 1:

4
Sample Output 1:

[1, 2, 'Fizz', 4]
Sample Input 2:

10
Sample Output 2:

[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']
 '''
  
  def generate_fizz_buzz_list(n):
    res_lst = []
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            res_lst.append('FizzBuzz')
            continue
        elif num % 3 == 0:
            res_lst.append('Fizz')
            continue
        elif num % 5 == 0:
            res_lst.append('Buzz')
            continue
        res_lst.append(num)
    
    return res_lst

n = int(input())
print(generate_fizz_buzz_list(n))
  
