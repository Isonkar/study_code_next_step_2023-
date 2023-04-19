''' обход элементов, замена местами строки и столбцы
'''

a = [
  [0, 2, 4, 6], 
  [1, 5, 9, 13],
  [3, 10, 17, 19]
]

for j in range(4):
    for i in range(3):
        print(a[i][j], end=' ')
    print()
 
#переворачиваем 
for i in range(2, -1, -1):
    for j in range(3, -1, -1):
        print(a[i][j], end=" ")
    print()
    
