'''
Напишите функцию shift_letter , которая принимает два аргумента:

letter одна английская буква в нижнем регистре
shift целое число - значение сдвига буквы (может быть как положительным, так и отрицательным)
Функция shift_letter  сдвигает символ letter вперед или назад на заданное значение shift .Сдвиг может быть цикличным в пределах от a до z. Ниже примеры:

shift_letter('b', 2)=> 'd'
shift_letter('d', 1) => 'e'
shift_letter('z', 1) => 'a'
shift_letter('d', -2) => 'b'
shift_letter('d', 26) => 'd'
shift_letter('b', -3) => 'y'
Не забудьте проаннотировать аргументы и также добавьте doc-строку «Функция сдвигает символ letter на shift позиций»

Функция shift_letter  должна вернуть новый символ. Вот вам в помощь ascii коды английских буквы, вам нужны только символы в нижнем регистре
'''

def shift_letter(letter: str, shift: int) -> str:
    'Функция сдвигает символ letter на shift позиций'  
    return chr((ord(letter) - ord('a') + shift) % 26 + 97)
  
# var 2

from string import ascii_lowercase

def shift_letter(letter: str, shift: int, alpha: str=ascii_lowercase) -> str:    
    """Функция сдвигает символ letter на shift позиций"""    
    return chr(ord(alpha[0]) + (ord(letter) - ord(alpha[0]) + shift) % len(alpha))
