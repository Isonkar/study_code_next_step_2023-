'''3/10 python add match (условная конструкция)'''

x, y = float(input()), float(input())
match input():
   case '+': n = x+y
   case '-': n = x-y
   case '*': n = x*y
   case '/' if y!=0: n = x/y
   case _: n = "Неизвестно"
print(n)
