'''
Cтрока S1 называется анаграммой строки S2, если она получается из S2 перестановкой символов.
Программа получает на вход две строки S1 и S2. Если строка S1 является анаграммой строки S2 нужно вывести YES, в противном случае - NO

Sample Input 1:
abc
cba
Sample Output 1:
YES

Sample Input 2:
abracadabra
cadabraabra
Sample Output 2:

YES
'''

string = input()

res_dict = {}
for i in range(len(string)):
    
        if res_dict.get(string[i], 0) == 0:
            res_dict[string[i]] = 1
        else:
            res_dict[string[i]] = res_dict.get(string[i]) + 1

string_1 = input()

res_dict_1 = {}
for i in range(len(string_1)):
    
        if res_dict_1.get(string_1[i], 0) == 0:
            res_dict_1[string_1[i]] = 1
        else:
            res_dict_1[string_1[i]] = res_dict_1.get(string_1[i]) + 1

if res_dict == res_dict_1:
    print('YES')
else:
    print('NO')

#  вариант два
print('YES' if sorted(input()) == sorted(input()) else 'NO')

