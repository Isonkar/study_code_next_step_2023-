'''
Ваша программа получает на вход последовательность фраз, указанных через запятую.
Для каждой фразы выведите слово ДА (в отдельной строке), если эта фраза ранее встречалось в последовательности или НЕТ, если не встречалось.
Символы во фразах нужно рассматривать без учета регистра, это значит что фраза Hasta la vista BAby эквивалента фразе hasta La Vista baby

Sample Input 1:
Hello world,hi dude,hello world,qwerty

Sample Output 1:
НЕТ
НЕТ
ДА
НЕТ
'''

words = list(map(str, input().lower().split(',')))

word_set = set()
for word in words:
    if word not in word_set:
        print('НЕТ')
        word_set.add(word)
    else:
        print('ДА')
