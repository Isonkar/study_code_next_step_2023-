'''
Напишите функцию only_one_positive, которая принимает произвольное количество числовых аргументов и возвращает True, когда из всех переданных значений только одно положительное, в противном случае верните False
Вам необходимо написать только определение функции only_one_positive
Ниже примеры вызова

only_one_positive(1, 2) -> False
only_one_positive(-1, 0, -3, 5, -3) -> True
only_one_positive() -> False
'''

def only_one_positive(*args: int) -> bool:
    cnt = 0
    for i in args:
        if i > 0:
            cnt += 1
    return True if cnt == 1 else False 

# var 2
def only_one_positive(*args):
    return len([x for x in args if x > 0]) == 1
