'''
В переменную starts_with присвойте lambda функцию, которая принимает строку и возвращает True, когда переданная строка начинается с буквы W. Во всех остальных случаях нужно возвращать False

Ничего кроме создания переменной starts_with делать не нужно

Sample Input 1:

World
Sample Output 1:

True
'''
starts_with = lambda x: True if x.startswith('W') else False
