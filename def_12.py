'''
Азотистые основания нуклеотидов ДНК
К азотистым основаниям относят аденин (A), гуанин (G), цитозин (C) и тимин (T), который входит в состав только ДНК. 
Они обладают схожими структурами и химическими свойствами. Это гетероциклические органические соединения, производные пиримидина и пурина, входящие в состав нуклеотидов. 
Аденин и гуанин — производные пурина, а цитозин и тимин — производные пиримидина.

В этой задаче вам необходимо создать функцию count_AGTC, которая принимает на вход строку - последовательность ДНК, состоящая только из символов A, G, T, C. 
Функция count_AGTC должна подсчитать количество каждого элемента в переданной последовательности и вернуть кортеж из найденных четырех количеств. Порядок элементов в кортеже должен быть именно таким A, G, T, C

count_AGTC('AGGTC') => (1, 2, 1, 1)
count_AGTC('AAAATTT') => (4, 0, 3, 0)
count_AGTC('AGTTTTT') => (1, 1, 5, 0)
count_AGTC('CCT') => (0, 0, 1, 2)
Нужно написать только определение функции count_AGTC 

Про инструкцию assert можно прочитать здесь

Sample Input:

Sample Output:

Проверки пройдены
'''

def count_AGTC(dna):
    dict_dna = {'A':0, 'G':0, 'T':0, 'C':0}
    temp_lst = []
  
    for elem in dna: 
        dict_dna[elem] = dna.count(elem)
    for el, cnt in dict_dna.items():
        temp_lst.append(cnt)
  
    return tuple(temp_lst)

# код ниже не стоит удалять, он нужен для проверки
assert count_AGTC('AGGTC') == (1, 2, 1, 1)
assert count_AGTC('AAAATTT') == (4, 0, 3, 0)
assert count_AGTC('AGTTTTT') == (1, 1, 5, 0)
assert count_AGTC('CCT') == (0, 0, 1, 2)     
print('Проверки пройдены')

# var 2

def count_AGTC(dna):
    return tuple(dna.count(k) for k in 'AGTC')
  
# var 3
def count_AGTC(dna):
    return dna.count('A'), dna.count('G'), dna.count('T'), dna.count('C')
