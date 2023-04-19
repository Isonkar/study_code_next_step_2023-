'''пример вложенного списка, обход элементов по значению + по индексу
'''

a = [
  [0, 2, 4, 6], 
  [1, 5, 9, 13],
  [3, 10, 17, 19]
]

# по значению
for i in a:
    for j in i:
        print(j, end=' ')
    print()
    
# по индексу

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
