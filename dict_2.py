'''
в1 добаляем d2, работает на python 3.9+
'''
d1 = {'India': 'Delhi',
      'Canada': 'Ottawa',
      'United States': 'Washington D. C.'}

d2 = {'France': 'Paris',
      'Malaysia': 'Kuala Lumpur'}

print(capitals := d1 | d2)
