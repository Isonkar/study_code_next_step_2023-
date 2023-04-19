'''сумма строк вложенного списка
'''

a = [
  [0, 2, 4, 6], 
  [1, 5, 9, 13], 
  [3, 10, 17, 19]
]
for i in range(3):
    sum = 0
    for j in range(4):
        sum += a[i][j]
    print(sum)
    
    
 # сумма столбцов
 a = [
  [0, 2, 4, 6], 
  [1, 5, 9, 13], 
  [3, 10, 17, 19]
]
for j in range(4):
    sum = 0
    for i in range(3):
        sum += a[i][j]
    print(sum)
    
