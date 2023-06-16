'''
Напишите функцию longest_word_in_file, которая принимает имя файла и внутри его содержимого находит самое длинное слово и возвращает его в качестве ответа. 
В случае,  если есть несколько слов с максимальной длиной, нужно вернуть слово, которое встречается последнее в тексте.

При этом слова в тексте отделяются друг от друга пробелами, любые другие знаки пунктуации необходимо исключить.  
И также учитывайте, что слова в тестах будут как на русском языке, так и на английском.

Если бы содержимое файла было таким:

He was running, but it was like running through deep water. There were trees all around him, 
trees which tried to stop him. They reached out with their branches. 
And it was behind him. It was coming nearer. 
то ответом было бы слово branches

Все возможные знаки пунктуации можно получить из модуля string

from string import punctuation

'''

from string import punctuation


def longest_word_in_file(file_name: str) -> str:
    data_list = []
    result_list = []
    with open(file_name, encoding='utf-8') as file:
        data_file = file.read().split()
    data_list = strip_file(data_file)
    x = data_list[0]
    for elem in data_list:
        if len(x) <= len(elem): 
            x = elem
            result_list.append(x)
          
    return result_list[-1]


def strip_file(data_file: list) -> list:
    result_list = []
    for elem in data_file:
        result_list.append(elem.strip(punctuation))
    return result_list
