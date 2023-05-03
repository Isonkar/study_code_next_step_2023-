'''
Во сколько обойдется данная покупка? Хотим купить все товары в указанном количестве
выводит итоговую сумму
'''

supermarket = {
    "milk": {"quantity": 20, "price": 1.19},
    "biscuits": {"quantity": 32, "price": 1.45},
    "butter": {"quantity": 20, "price": 2.29},
    "cheese": {"quantity": 15, "price": 1.90},
    "bread": {"quantity": 15, "price": 2.59},
    "cookies": {"quantity": 20, "price": 4.99},
    "yogurt": {"quantity": 18, "price": 3.65},
    "apples": {"quantity": 35, "price": 3.15},
    "oranges": {"quantity": 40, "price": 0.99},
    "bananas": {"quantity": 23, "price": 1.29}
}
total = 0
for item in supermarket:
    total += supermarket[item]['quantity'] * supermarket[item]['price']
print(total)

#  вариант два печатает как чек
supermarket = {
    "milk": {"quantity": 20, "price": 1.19},
    "biscuits": {"quantity": 32, "price": 1.45},
    "butter": {"quantity": 20, "price": 2.29},
    "cheese": {"quantity": 15, "price": 1.90},
    "bread": {"quantity": 15, "price": 2.59},
    "cookies": {"quantity": 20, "price": 4.99},
    "yogurt": {"quantity": 18, "price": 3.65},
    "apples": {"quantity": 35, "price": 3.15},
    "oranges": {"quantity": 40, "price": 0.99},
    "bananas": {"quantity": 23, "price": 1.29}
}
print('-' * 41)
sum_p = 0
for p, q in supermarket.items():
    print(f"{p:<15}{q['quantity']} шт. * {q['price']:>5.2f}₽{'=':>5}{q['quantity'] * q['price']:.2f}₽")
    sum_p += q['quantity'] * q['price']

print('-' * 41)
print(f"ИТОГ: {'=':>28}{sum_p:.2f}₽")
print(f'{"СПАСИБО ЗА ПОКУПКУ!":^41}')

#  вариант три

